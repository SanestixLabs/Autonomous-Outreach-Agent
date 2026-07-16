from pydantic import BaseModel, Field

from company_analysis_agent.schema import CompanyAnalysis
from lead_qualification_agent.schema import LeadQualification
from service_recommendation_agent.schema import ServiceRecommendation


class PersonalizedEmailInput(BaseModel):
    company_analysis: CompanyAnalysis = Field(
        description="The analyzed company information."
    )

    lead_qualification: LeadQualification = Field(
        description="The lead qualification result."
    )

    service_recommendation: ServiceRecommendation = Field(
        description="The recommended AI services for the company."
    )


class PersonalizedEmail(BaseModel):
    subject: str = Field(
        description="Professional email subject line."
    )

    email_body: str = Field(
        description="Personalized outreach email."
    )