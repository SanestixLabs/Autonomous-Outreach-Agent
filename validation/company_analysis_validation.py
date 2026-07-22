from company_analysis_agent.schema import CompanyAnalysis


def validate_company_analysis(result: CompanyAnalysis):
    errors = []
    warnings = []

    if not result.company_name:
        errors.append("Company name is missing.")

    if not result.industry:
        errors.append("Industry is missing.")

    if not result.company_size:
        warnings.append("Company size is missing.")

    if not result.products_services:
        warnings.append("No products or services identified.")

    if not result.target_customers:
        warnings.append("No target customers identified.")

    if not result.pain_points:
        warnings.append("No pain points identified.")

    if not result.technologies:
        warnings.append("No technologies identified.")

    if not result.business_summary:
        warnings.append("Business summary is missing.")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }