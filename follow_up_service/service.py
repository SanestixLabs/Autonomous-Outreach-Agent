from common.enums import WorkflowType

from follow_up_service.rules import should_follow_up
from follow_up_service.schema import (
    FollowUpContext,
    FollowUpDecision,
    FollowUpStatus,
)


class FollowUpService:
    """
    Service responsible for evaluating whether a lead requires follow-up.
    """

    def evaluate_follow_up(self, context: FollowUpContext) -> FollowUpDecision:
        """
        Evaluate the follow-up context and return a follow-up decision.
        """
        result = should_follow_up(context)

        if result.follow_up_required:
            return FollowUpDecision(
                status=FollowUpStatus.REQUIRED,
                reason=result.reason,
                recommended_workflow=WorkflowType.PERSONALIZED_EMAIL,
            )

        return FollowUpDecision(
            status=FollowUpStatus.NOT_REQUIRED,
            reason=result.reason,
            recommended_workflow=None,
        )