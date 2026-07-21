from lead_qualification_agent.schema import LeadQualification


def validate_lead_qualification(result: LeadQualification):
    errors = []
    warnings = []

    if not isinstance(result.qualified, bool):
        errors.append("Qualified must be a boolean value.")

    if not (0 <= result.score <= 100):
        errors.append("Lead score must be between 0 and 100.")

    if result.priority not in ["High", "Medium", "Low"]:
        errors.append("Priority must be High, Medium, or Low.")

    if not result.reason:
        warnings.append("Qualification reason is missing.")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }