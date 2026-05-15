from ollama import chat
from app.config import MODEL_NAME, SYSTEM_PROMPT
from app.memory.store import load_memory

def generate_response(user_input: str) -> str:
    memory = load_memory()

    memory_context = f"""
Last task: {memory['last_task']}
Last state: {memory['last_state']}
Recent actions: {memory['recent_actions']}
"""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT + "\n" + memory_context,
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