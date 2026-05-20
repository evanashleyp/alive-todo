def detect_task_type(user_input: str) -> str:
    text = user_input.lower()

    technical_keywords = [
        "architecture",
        "system",
        "queue",
        "worker",
        "agent",
        "async",
        "memory",
        "model",
    ]

    emotional_keywords = [
        "capek",
        "bingung",
        "overwhelmed",
        "tired",
        "sedih",
    ]

    creative_keywords = [
        "idea",
        "imagine",
        "story",
        "design",
    ]

    if any(word in text for word in technical_keywords):
        return "technical_design"

    if any(word in text for word in emotional_keywords):
        return "emotional_reflection"

    if any(word in text for word in creative_keywords):
        return "creative_exploration"

    return "general_reflection"