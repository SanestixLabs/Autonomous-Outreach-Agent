from enum import Enum

from pydantic import BaseModel, Field


class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class LeadQualification(BaseModel):
    qualified: bool = Field(
        description="Whether the company is a qualified sales lead."
    )

    score: int = Field(
        ge=0,
        le=100,
        description="Lead qualification score between 0 and 100."
    )

    priority: Priority = Field(
        description="Lead priority level."
    )

    reason: str = Field(
        description="Reason for the qualification decision."
    )