from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from company_analysis_agent.schema import CompanyAnalysis
from lead_qualification_agent.schema import LeadQualification
from personalized_email_agent.schema import PersonalizedEmail
from service_recommendation_agent.schema import ServiceRecommendation


class LeadState(str, Enum):
    NEW = "New"
    CONTACTED = "Contacted"
    FOLLOW_UP_REQUIRED = "Follow-up Required"
    MEETING_BOOKED = "Meeting Booked"
    CONVERTED = "Converted"
    CLOSED = "Closed"


class WorkflowStatus(str, Enum):
    SUCCESS = "Success"
    FAILED = "Failed"
    SKIPPED = "Skipped"


class InteractionHistory(BaseModel):
    last_contacted_at: datetime | None = Field(
        default=None,
        description="Timestamp of the most recent outreach."
    )

    reply_received: bool = Field(
        default=False,
        description="Whether the lead has replied."
    )

    meeting_booked: bool = Field(
        default=False,
        description="Whether a meeting has been booked."
    )

    follow_up_count: int = Field(
        default=0,
        ge=0,
        description="Number of follow-up emails sent."
    )


class WorkflowExecution(BaseModel):
    workflow_name: str = Field(
        description="Name of the executed workflow."
    )

    status: WorkflowStatus = Field(
        description="Execution status."
    )

    executed_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when the workflow was executed."
    )


class CachedOutputs(BaseModel):
    company_analysis: CompanyAnalysis | None = Field(
        default=None,
        description="Cached company analysis result."
    )

    lead_qualification: LeadQualification | None = Field(
        default=None,
        description="Cached lead qualification result."
    )

    service_recommendation: ServiceRecommendation | None = Field(
        default=None,
        description="Cached AI service recommendations."
    )

    personalized_email: PersonalizedEmail | None = Field(
        default=None,
        description="Cached personalized outreach email."
    )


class LeadMemory(BaseModel):
    lead_id: str = Field(
        description="Unique identifier for the lead."
    )

    company_name: str = Field(
        description="Name of the company."
    )

    lead_state: LeadState = Field(
        default=LeadState.NEW,
        description="Current lifecycle stage of the lead."
    )

    interaction_history: InteractionHistory = Field(
        default_factory=InteractionHistory,
        description="History of interactions with the lead."
    )

    cached_outputs: CachedOutputs = Field(
        default_factory=CachedOutputs,
        description="Previously generated agent outputs."
    )

    workflow_history: list[WorkflowExecution] = Field(
        default_factory=list,
        description="History of executed workflows."
    )

    last_workflow: str | None = Field(
        default=None,
        description="Most recently executed workflow."
    )