from company_analysis_agent.schema import CompanyAnalysis


def evaluate_company_analysis(result: CompanyAnalysis):
    score = 100
    feedback = []

    if not result.company_name:
        score -= 15
        feedback.append("Missing company name.")

    if not result.industry:
        score -= 10
        feedback.append("Missing industry.")

    if not result.company_size:
        score -= 10
        feedback.append("Missing company size.")

    if not result.products_services:
        score -= 15
        feedback.append("No products/services identified.")

    if not result.target_customers:
        score -= 10
        feedback.append("No target customers identified.")

    if not result.pain_points:
        score -= 20
        feedback.append("No pain points identified.")

    if not result.technologies:
        score -= 10
        feedback.append("No technologies identified.")

    if not result.business_summary:
        score -= 10
        feedback.append("Business summary missing.")

    return {
        "passed": score >= 80,
        "score": score,
        "feedback": feedback
    }