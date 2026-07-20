from evaluation.company_analysis_eval import evaluate_company_analysis
from evaluation.lead_qualification_eval import evaluate_lead_qualification
from evaluation.service_recommendation_eval import (
    evaluate_service_recommendation,
)
from evaluation.personalized_email_eval import (
    evaluate_personalized_email,
)


def evaluate_pipeline(
    company_analysis,
    lead_qualification,
    service_recommendation,
    personalized_email,
):
    company_result = evaluate_company_analysis(company_analysis)
    lead_result = evaluate_lead_qualification(lead_qualification)
    service_result = evaluate_service_recommendation(service_recommendation)
    email_result = evaluate_personalized_email(personalized_email)

    overall_score = (
        company_result["score"]
        + lead_result["score"]
        + service_result["score"]
        + email_result["score"]
    ) / 4

    pipeline_passed = (
        company_result["passed"]
        and lead_result["passed"]
        and service_result["passed"]
        and email_result["passed"]
    )

    return {
        "company_analysis": company_result,
        "lead_qualification": lead_result,
        "service_recommendation": service_result,
        "personalized_email": email_result,
        "overall_score": round(overall_score, 2),
        "pipeline_passed": pipeline_passed,
    }