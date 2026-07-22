from guardrails.rules import (
    FORBIDDEN_EMAIL_PHRASES,
    VALID_PRIORITIES,
)


def check_company_analysis(company):
    violations = []

    if not company.company_name:
        violations.append("Missing company name.")

    if not company.industry:
        violations.append("Missing industry.")

    return violations


def check_lead_qualification(lead):
    violations = []

    if not (0 <= lead.score <= 100):
        violations.append("Invalid lead score.")

    if lead.priority not in VALID_PRIORITIES:
        violations.append("Invalid priority.")

    return violations


def check_service_recommendation(service):
    violations = []

    if not service.recommendations:
        violations.append("No recommendations generated.")

    return violations


def check_personalized_email(email):
    violations = []

    text = email.email_body.lower()

    for phrase in FORBIDDEN_EMAIL_PHRASES:
        if phrase in text:
            violations.append(
                f"Forbidden phrase detected: '{phrase}'."
            )

    return violations


def run_guardrails(
    company,
    lead,
    service,
    email,
):
    violations = []

    # Individual guardrails
    violations.extend(check_company_analysis(company))
    violations.extend(check_lead_qualification(lead))
    violations.extend(check_service_recommendation(service))
    violations.extend(check_personalized_email(email))

    # Pipeline business rules

    if not lead.qualified and service.recommendations:
        violations.append(
            "Unqualified leads should not receive service recommendations."
        )

    if lead.qualified and not service.recommendations:
        violations.append(
            "Qualified lead has no service recommendations."
        )

    if not service.recommendations and email.email_body:
        violations.append(
            "Email generated without service recommendations."
        )

    if lead.score < 50 and lead.priority == "High":
        violations.append(
            "Lead score and priority are inconsistent."
        )

    return {
        "passed": len(violations) == 0,
        "violations": violations,
    }