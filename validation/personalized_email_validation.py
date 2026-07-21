from personalized_email_agent.schema import PersonalizedEmail


def validate_personalized_email(result: PersonalizedEmail):
    errors = []
    warnings = []

    if not result.subject:
        errors.append("Email subject is missing.")

    if not result.email_body:
        errors.append("Email body is missing.")

    else:
        email = result.email_body.lower()

        if "dear" not in email:
            warnings.append("Greeting is missing.")

        if "regards" not in email:
            warnings.append("Closing is missing.")

        if "sanestix" not in email:
            warnings.append("Sanestix is not mentioned.")

        if "call" not in email and "meeting" not in email:
            warnings.append("Call-to-action is missing.")

    return {
        "agent": "Personalized Email",
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }