from typing import List

from pydantic import BaseModel, Field

from company_analysis_agent.schema import CompanyAnalysis
from lead_qualification_agent.schema import LeadQualification, Priority


class ServiceRecommendationInput(BaseModel):
    company_analysis: CompanyAnalysis = Field(
        description="The analyzed company information."
    )

    lead_qualification: LeadQualification = Field(
        description="The lead qualification result."
    )


class Recommendation(BaseModel):
    service_name: str = Field(
        description="Recommended AI service."
    )

    priority: Priority = Field(
        description="Priority of implementing this service."
    )

    reason: str = Field(
        description="Reason why this service is recommended."
    )

    estimated_impact: str = Field(
        description="Expected business impact of implementing this service."
    )


class ServiceRecommendation(BaseModel):
    recommendations: List[Recommendation] = Field(
        description="List of AI service recommendations for the company."
    )