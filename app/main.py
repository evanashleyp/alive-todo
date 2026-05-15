from app.llm.client import generate_response


def main():
    print("Alive Todo started.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Alive Todo stopped.")
            break

        response = generate_response(user_input)

        print(f"\nAlive: {response}\n")


if __name__ == "__main__":
    main()