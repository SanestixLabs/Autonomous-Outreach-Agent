from service_recommendation_agent.schema import ServiceRecommendation


def validate_service_recommendation(result: ServiceRecommendation):
    errors = []
    warnings = []

    if not result.recommendations:
        errors.append("No service recommendations generated.")

    else:
        for index, recommendation in enumerate(result.recommendations, start=1):

            if not recommendation.service_name:
                errors.append(
                    f"Recommendation {index}: Missing service name."
                )

            if recommendation.priority not in ["High", "Medium", "Low"]:
                errors.append(
                    f"Recommendation {index}: Invalid priority."
                )

            if not recommendation.reason:
                warnings.append(
                    f"Recommendation {index}: Missing reason."
                )

            if not recommendation.estimated_impact:
                warnings.append(
                    f"Recommendation {index}: Missing estimated impact."
                )

    return {
        "agent": "Service Recommendation",
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }