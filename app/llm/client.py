from ollama import chat
from app.config import MODEL_NAME, SYSTEM_PROMPT
from app.memory.store import load_memory
from app.modes.detector import detect_mode

def generate_response(user_input: str) -> str:
    memory = load_memory()

    mode = detect_mode(user_input)

    memory_context = f"""
Current focus: {memory['current_focus']}
Energy state: {memory['energy_state']}
Recent topics: {memory['recent_topics']}
Active tasks: {memory['active_tasks']}
completed thoughts: {memory['completed_thoughts']}
"""


    mode_context = ""
    if mode == "low_energy":
        mode_context = """
        The user seems tired or overwhelmed.

        Lower expectations.
        Suggest rest or very small actions.
        Speak softer and slower.
        """
    elif mode == "gentle_start":
        mode_context = """
    The user seems stuck or procrastinating.

    Help them begin with the smallest possible step.
    Normalize resistance.
    Avoid pressure.
    """

    elif mode == "focus_flow":
        mode_context = """
    The user is already working.

    Encourage continuation gently.
    Do not interrupt momentum.
    """

    elif mode == "reflection":
        mode_context = """
    The interaction is winding down.

    Acknowledge effort softly.
    Avoid productivity language.
    """

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT + "\n" + memory_context + "\n" + mode_context,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
        options={
            "temperature": 0.7,
        }
    )

    return response["message"]["content"]