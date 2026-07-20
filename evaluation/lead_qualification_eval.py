from lead_qualification_agent.schema import LeadQualification


def evaluate_lead_qualification(result: LeadQualification):
    score = 100
    feedback = []

    if result.score < 0 or result.score > 100:
        score -= 30
        feedback.append("Lead score must be between 0 and 100.")

    if result.priority not in ["High", "Medium", "Low"]:
        score -= 20
        feedback.append("Invalid priority level.")

    if not result.reason:
        score -= 20
        feedback.append("Reason is missing.")

    if not isinstance(result.qualified, bool):
        score -= 30
        feedback.append("Qualified must be True or False.")

    return {
        "passed": score >= 80,
        "score": score,
        "feedback": feedback
    }