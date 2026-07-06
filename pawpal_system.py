from dataclasses import dataclass, field
from typing import List


class Owner:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.pets: List["Pet"] = []

    def add_pet(self, pet: "Pet"):
        self.pets.append(pet)

    def get_all_tasks(self) -> List["Task"]:
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def update_info(self):
        pass


@dataclass
class Pet:
    name: str
    age: int
    breed: str
    owner: Owner
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task"):
        self.tasks.append(task)

    def update_info(self):
        pass


@dataclass
class Task:
    task_type: str
    time_to_complete: int
    priority: str
    pet: Pet
    frequency: str = "daily"
    is_completed: bool = False

    def change_priority(self, new_priority: str):
        self.priority = new_priority

    def mark_completed(self):
        self.is_completed = True


class Schedule:
    def __init__(self, owner: Owner, time_available: int):
        self.owner = owner
        self.time_available = time_available
        self.scheduled_tasks: List[Task] = []

    def create_schedule(self):
        all_tasks = self.owner.get_all_tasks()
        pending_tasks = [task for task in all_tasks if not task.is_completed]

        priority_order = {"high": 0, "medium": 1, "low": 2}
        sorted_tasks = sorted(
            pending_tasks,
            key=lambda task: priority_order.get(task.priority, 3),
        )

        self.scheduled_tasks = []
        remaining_time = self.time_available
        for task in sorted_tasks:
            if task.time_to_complete <= remaining_time:
                self.scheduled_tasks.append(task)
                remaining_time -= task.time_to_complete

        return self.scheduled_tasks

    def update_schedule(self):
        self.create_schedule()

    def explain(self):
        explanations = []
        for task in self.scheduled_tasks:
            explanations.append(
                f"{task.pet.name}: {task.task_type} "
                f"({task.priority} priority, {task.time_to_complete} min)"
            )
        return explanations
