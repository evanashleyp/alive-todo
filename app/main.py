from statistics import mode

from app.llm.client import generate_response
from app.memory.store import load_memory, save_memory
from app.modes.detector import detect_mode

def main():
    print("Alive Todo started.\n")

    while True:
        user_input = input("You: ")


        if user_input.lower() in ["exit", "quit"]:
            print("Alive Todo stopped.")
            break

        mode = detect_mode(user_input)
        print(f"[Mode: {mode}]")
        
        response = generate_response(user_input)

        memory = load_memory()

        memory["last_task"] = user_input
        memory["last_state"] = "working"

        memory["recent_actions"].append(user_input)

        memory["recent_actions"] = memory["recent_actions"][-5:]

        save_memory(memory)

        print(f"\nAlive: {response}\n")


if __name__ == "__main__":
    main()