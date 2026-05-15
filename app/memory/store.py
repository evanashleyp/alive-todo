import json
from pathlib import Path

MEMORY_PATH = Path("data/memory.json")


def load_memory():
    with open(MEMORY_PATH, "r") as file:
        return json.load(file)


def save_memory(memory_data):
    with open(MEMORY_PATH, "w") as file:
        json.dump(memory_data, file, indent=2)