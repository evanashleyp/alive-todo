import time

from app.queue.task_queue import task_queue, completed_tasks
from app.llm.client import generate_response


def start_worker():
    while True:
        task = task_queue.get()

        if task is None:
            break

        user_input = task["content"]

        time.sleep(5)

        response = generate_response(user_input)

        completed_tasks.append({
            "id": task["id"],
            "response": response,
            "task_content": task["content"],
        })

        task_queue.task_done()