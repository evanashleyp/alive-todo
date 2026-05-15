from ollama import chat
from app.config import MODEL_NAME, SYSTEM_PROMPT


def generate_response(user_input: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )

    return response["message"]["content"]