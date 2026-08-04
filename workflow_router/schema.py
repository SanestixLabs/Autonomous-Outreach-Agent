from enum import Enum

from pydantic import BaseModel, Field

from common.enums import WorkflowType
from follow_up_service.schema import FollowUpDecision


class PipelineStage(str, Enum):
    INITIAL = "Initial"
    COMPANY_ANALYZED = "Company Analyzed"
    LEAD_QUALIFIED = "Lead Qualified"
    SERVICE_RECOMMENDED = "Service Recommended"
    EMAIL_GENERATED = "Email Generated"
    COMPLETED = "Completed"


class RouteContext(BaseModel):
    pipeline_stage: PipelineStage | None = Field(
        default=None,
        description="Current AI pipeline stage for new leads."
    )

    follow_up_decision: FollowUpDecision | None = Field(
        default=None,
        description="Follow-up decision for existing leads."
    )


class RoutingDecision(BaseModel):
    next_workflow: WorkflowType | None = Field(
        default=None,
        description="Next workflow to execute."
    )

    reason: str = Field(
        description="Reason for the routing decision."
    )