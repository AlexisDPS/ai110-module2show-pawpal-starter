from dataclasses import dataclass
from typing import List


class Owner:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def update_info(self):
        pass


@dataclass
class Pet:
    name: str
    age: int
    breed: str
    owner: Owner

    def update_info(self):
        pass


@dataclass
class Task:
    task_type: str
    time_to_complete: int
    priority: str
    pet: Pet

    def change_priority(self):
        pass


class Schedule:
    def __init__(self, tasks: List[Task], owner: Owner, time_available: int):
        self.tasks = tasks
        self.owner = owner
        self.time_available = time_available

    def create_schedule(self, tasks, time_available):
        pass

    def update_schedule(self):
        pass

    def explain(self):
        pass
