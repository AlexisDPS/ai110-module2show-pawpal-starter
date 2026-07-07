from datetime import datetime

from pawpal_system import Owner, Pet, Task, Schedule

owner = Owner(name="Jordan", age=30)

biscuit = Pet(name="Biscuit", age=3, breed="Golden Retriever", owner=owner)
mochi = Pet(name="Mochi", age=2, breed="Tabby Cat", owner=owner)

owner.add_pet(biscuit)
owner.add_pet(mochi)

biscuit.add_task(Task(task_type="Feeding", time_to_complete=10, priority="high", pet=biscuit))
mochi.add_task(Task(task_type="Playtime", time_to_complete=20, priority="low", pet=mochi))
mochi.add_task(Task(task_type="Litter box cleaning", time_to_complete=15, priority="medium", pet=mochi))
biscuit.add_task(Task(task_type="Morning walk", time_to_complete=30, priority="high", pet=biscuit))

# Two tasks (different pets) due at the exact same time, to demonstrate conflict detection
same_time = datetime(2026, 7, 8, 8, 0)
biscuit.add_task(Task(task_type="Vet checkup", time_to_complete=30, priority="high", pet=biscuit, due_date=same_time))
mochi.add_task(Task(task_type="Grooming", time_to_complete=30, priority="medium", pet=mochi, due_date=same_time))

# Mark one task complete so filtering has something to show
mochi.tasks[1].mark_complete()

schedule = Schedule(owner=owner, time_available=60)
schedule.create_schedule()

print("Today's Schedule")
print("-----------------")
for reason in schedule.explain():
    print(reason)

print("\nAll Tasks Sorted by Time")
print("-------------------------")
for task in schedule.sort_by_time(owner.get_all_tasks()):
    print(f"{task.pet.name}: {task.task_type} ({task.time_to_complete} min)")

print("\nCompleted Tasks")
print("----------------")
for task in schedule.filter_tasks(is_completed=True):
    print(f"{task.pet.name}: {task.task_type}")

print("\nMochi's Tasks")
print("--------------")
for task in schedule.filter_tasks(pet_name="Mochi"):
    status = "done" if task.is_completed else "pending"
    due = task.due_date.strftime("%Y-%m-%d")
    print(f"{task.task_type} ({status}, due {due})")

print("\nScheduling Conflicts")
print("---------------------")
warnings = schedule.find_conflicts()
if warnings:
    for warning in warnings:
        print(warning)
else:
    print("No conflicts found.")
