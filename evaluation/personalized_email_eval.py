from personalized_email_agent.schema import PersonalizedEmail


def evaluate_personalized_email(result: PersonalizedEmail):
    score = 100
    feedback = []

    if not result.subject:
        score -= 20
        feedback.append("Email subject is missing.")

    if not result.email_body:
        score -= 40
        feedback.append("Email body is missing.")

    else:
        email = result.email_body.lower()

        if "dear" not in email:
            score -= 10
            feedback.append("Greeting is missing.")

        if "best regards" not in email and "regards" not in email:
            score -= 10
            feedback.append("Closing is missing.")

        if "sanestix" not in email:
            score -= 10
            feedback.append("Company name 'Sanestix' is not mentioned.")

        if "call" not in email and "meeting" not in email:
            score -= 10
            feedback.append("Call-to-action is missing.")

    return {
        "passed": score >= 80,
        "score": max(score, 0),
        "feedback": feedback
    }