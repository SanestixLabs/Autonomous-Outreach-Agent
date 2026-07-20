from service_recommendation_agent.schema import ServiceRecommendation


def evaluate_service_recommendation(result: ServiceRecommendation):
    score = 100
    feedback = []

    if not result.recommendations:
        score -= 50
        feedback.append("No service recommendations generated.")

    else:
        for index, recommendation in enumerate(result.recommendations, start=1):

            if not recommendation.service_name:
                score -= 10
                feedback.append(
                    f"Recommendation {index}: Missing service name."
                )

            if recommendation.priority not in ["High", "Medium", "Low"]:
                score -= 10
                feedback.append(
                    f"Recommendation {index}: Invalid priority."
                )

            if not recommendation.reason:
                score -= 10
                feedback.append(
                    f"Recommendation {index}: Missing reason."
                )

            if not recommendation.estimated_impact:
                score -= 10
                feedback.append(
                    f"Recommendation {index}: Missing estimated impact."
                )

    return {
        "passed": score >= 80,
        "score": max(score, 0),
        "feedback": feedback
    }