from validation.company_analysis_validation import (
    validate_company_analysis,
)
from validation.lead_qualification_validation import (
    validate_lead_qualification,
)
from validation.service_recommendation_validation import (
    validate_service_recommendation,
)
from validation.personalized_email_validation import (
    validate_personalized_email,
)


def validate_pipeline(
    company_analysis,
    lead_qualification,
    service_recommendation,
    personalized_email,
):
    company_result = validate_company_analysis(company_analysis)
    lead_result = validate_lead_qualification(lead_qualification)
    service_result = validate_service_recommendation(
        service_recommendation
    )
    email_result = validate_personalized_email(
        personalized_email
    )

    pipeline_valid = (
        company_result["valid"]
        and lead_result["valid"]
        and service_result["valid"]
        and email_result["valid"]
    )

    return {
        "pipeline_valid": pipeline_valid,
        "results": [
            company_result,
            lead_result,
            service_result,
            email_result,
        ],
    }