from app.llm.client import generate_response
from app.memory.store import load_memory, save_memory
from app.modes.detector import detect_mode

import threading

from app.queue.worker import start_worker
from app.queue.task_queue import task_queue, completed_tasks

import time

from app.tasks.router import detect_task_type


def main():
    memory = load_memory()
    print("Alive Todo started.\n")

    worker_thread = threading.Thread(target=start_worker, daemon=True)
    worker_thread.start()

    while True:
        while completed_tasks:
            completed = completed_tasks.pop(0)

            task_content = completed["task_content"]

            if task_content in memory["active_tasks"]:
                memory["active_tasks"].remove(task_content)

            memory["completed_thoughts"].append(task_content)

            memory["completed_thoughts"] = memory["completed_thoughts"][-5:]

            save_memory(memory)

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

        task_type = detect_task_type(user_input)
        print(f"[Task Type: {task_type}]")

        if "deep" in user_input.lower() or "architecture" in user_input.lower():

            from app.queue import task_queue as queue_state

            queue_state.task_counter += 1

            task = {
                "id": queue_state.task_counter,
                "type": task_type,
                "content": user_input,
                "created_at": time.time(),
                "mode": mode,
                "context": {
                    "focus": memory["current_focus"],
                    "recent_topics": memory["recent_topics"],
                    "energy_state": memory["energy_state"],
                },
            }

            memory["active_tasks"].append(task["content"])

            memory["active_tasks"] = memory["active_tasks"][-5:]
            
            print(f"\nAlive: aku pikirin dulu ya... [task #{task['id']}]\n")

            task_queue.put(task)

            memory["current_focus"] = user_input

            save_memory(memory)

            continue
        
        response = generate_response(user_input)


        memory["current_focus"] = user_input

        if mode == "low_energy":
            memory["energy_state"] = "low"

        elif mode == "focus_flow":
            memory["energy_state"] = "focused"

        else:
            memory["energy_state"] = "neutral"


        memory["recent_topics"].append(user_input)

        memory["recent_topics"] = memory["recent_topics"][-5:]

        save_memory(memory)

        print(f"\nAlive: {response}\n")


if __name__ == "__main__":
    main()