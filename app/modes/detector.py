def detect_mode(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in ["capek", "lelah", "tired", "burnout"]):
        return "low_energy"

    if any(word in text for word in ["bingung", "stuck", "ga mulai", "malas"]):
        return "gentle_start"

    if any(word in text for word in ["lanjut", "ngerjain", "fokus"]):
        return "focus_flow"

    if any(word in text for word in ["selesai", "udah", "goodnight"]):
        return "reflection"

    return "default"