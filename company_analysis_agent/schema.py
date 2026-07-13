from pydantic import BaseModel, Field


class CompanyAnalysis(BaseModel):
    company_name: str = Field(
        description="Name of the company."
    )

    industry: str = Field(
        description="Industry the company operates in."
    )

    company_size: str = Field(
        description="Estimated company size."
    )

    products_services: list[str] = Field(
        description="Products or services offered by the company."
    )

    target_customers: list[str] = Field(
        description="Primary target customers."
    )

    pain_points: list[str] = Field(
        description="Business challenges or pain points identified."
    )

    technologies: list[str] = Field(
        description="Technologies currently used by the company."
    )

    business_summary: str = Field(
        description="A concise summary of the company's business."
    )
