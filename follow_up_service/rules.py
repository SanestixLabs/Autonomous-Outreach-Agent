from pydantic import BaseModel

from follow_up_service.schema import FollowUpContext
from memory_service.schema import LeadState


MAX_FOLLOW_UPS = 3
MIN_WAIT_DAYS = 5


class RuleResult(BaseModel):
    follow_up_required: bool
    reason: str


def is_lead_eligible(context: FollowUpContext) -> bool:
    """
    Determine whether the lead is eligible for follow-up.
    """
    return context.lead_state not in (
        LeadState.CLOSED,
        LeadState.CONVERTED,
    )


def has_reply(context: FollowUpContext) -> bool:
    """
    Check whether the lead has replied.
    """
    return context.business_signals.reply_received


def has_meeting(context: FollowUpContext) -> bool:
    """
    Check whether a meeting has already been booked.
    """
    return context.business_signals.meeting_booked


def is_converted(context: FollowUpContext) -> bool:
    """
    Check whether the lead has already converted.
    """
    return context.business_signals.lead_converted


def max_followups_reached(context: FollowUpContext) -> bool:
    """
    Check whether the maximum number of follow-ups has been reached.
    """
    return context.follow_up_count >= MAX_FOLLOW_UPS


def waiting_period_elapsed(context: FollowUpContext) -> bool:
    """
    Check whether the minimum waiting period has elapsed.
    """
    return context.days_since_last_contact >= MIN_WAIT_DAYS


def should_follow_up(context: FollowUpContext) -> RuleResult:
    """
    Evaluate all follow-up rules and return the decision.
    """

    if not is_lead_eligible(context):
        return RuleResult(
            follow_up_required=False,
            reason="Lead is not eligible for follow-up."
        )

    if is_converted(context):
        return RuleResult(
            follow_up_required=False,
            reason="Lead has already been converted."
        )

    if has_reply(context):
        return RuleResult(
            follow_up_required=False,
            reason="Lead has already replied."
        )

    if has_meeting(context):
        return RuleResult(
            follow_up_required=False,
            reason="A meeting has already been booked."
        )

    if max_followups_reached(context):
        return RuleResult(
            follow_up_required=False,
            reason="Maximum number of follow-up attempts reached."
        )

    if not waiting_period_elapsed(context):
        return RuleResult(
            follow_up_required=False,
            reason="Minimum waiting period has not elapsed."
        )

    return RuleResult(
        follow_up_required=True,
        reason="Lead is eligible for follow-up."
    )