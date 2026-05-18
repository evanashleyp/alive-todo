from statistics import mode

from app.llm.client import generate_response
from app.memory.store import load_memory, save_memory
from app.modes.detector import detect_mode

import threading

from app.queue.worker import start_worker
from app.queue.task_queue import task_queue, completed_tasks

import time

def main():
    print("Alive Todo started.\n")

    worker_thread = threading.Thread(target=start_worker, daemon=True)
    worker_thread.start()

    while True:
        while completed_tasks:
            completed = completed_tasks.pop(0)

            print(
                f"\nAlive (async) [task #{completed['id']}]: "
                f"{completed['response']}\n"
            )

        user_input = input("You: ")


        if user_input.lower() in ["exit", "quit"]:
            print("Alive Todo stopped.")
            break

        mode = detect_mode(user_input)
        print(f"[Mode: {mode}]")

        if "deep" in user_input.lower() or "architecture" in user_input.lower():

            from app.queue import task_queue as queue_state

            queue_state.task_counter += 1

            task = {
                "id": queue_state.task_counter,
                "type": "deep_thought",
                "content": user_input,
                "created_at": time.time(),
                "mode": mode,
            }
            
            print(f"\nAlive: aku pikirin dulu ya... [task #{task['id']}]\n")

            task_queue.put(task)

            continue
        
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