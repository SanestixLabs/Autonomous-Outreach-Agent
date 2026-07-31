from enum import Enum

from pydantic import BaseModel, Field

from common.enums import WorkflowType
from memory_service.schema import LeadState, WorkflowExecution


class FollowUpStatus(str, Enum):
    REQUIRED = "Required"
    NOT_REQUIRED = "Not Required"


class BusinessSignals(BaseModel):
    reply_received: bool = Field(
        default=False,
        description="Whether the lead has replied to previous outreach."
    )

    meeting_booked: bool = Field(
        default=False,
        description="Whether a meeting has been scheduled."
    )

    lead_converted: bool = Field(
        default=False,
        description="Whether the lead has already been converted into a customer."
    )


class FollowUpContext(BaseModel):
    lead_state: LeadState = Field(
        description="Current lifecycle state of the lead."
    )

    workflow_history: list[WorkflowExecution] = Field(
        default_factory=list,
        description="History of executed workflows."
    )

    last_workflow: WorkflowType | None = Field(
        default=None,
        description="Most recently executed workflow."
    )

    days_since_last_contact: int = Field(
        ge=0,
        description="Number of days since the last outreach."
    )

    follow_up_count: int = Field(
        default=0,
        ge=0,
        description="Number of follow-up attempts already made."
    )

    business_signals: BusinessSignals = Field(
        default_factory=BusinessSignals,
        description="Business signals retrieved from external systems."
    )


class FollowUpDecision(BaseModel):
    status: FollowUpStatus = Field(
        description="Whether a follow-up is required."
    )

    reason: str = Field(
        description="Reason for the decision."
    )

    recommended_workflow: WorkflowType | None = Field(
        default=None,
        description="Workflow recommended by the Follow-up Service."
    )