from pawpal_system import Owner, Pet, Task, Schedule

owner = Owner(name="Jordan", age=30)

biscuit = Pet(name="Biscuit", age=3, breed="Golden Retriever", owner=owner)
mochi = Pet(name="Mochi", age=2, breed="Tabby Cat", owner=owner)

owner.add_pet(biscuit)
owner.add_pet(mochi)

biscuit.add_task(Task(task_type="Morning walk", time_to_complete=30, priority="high", pet=biscuit))
biscuit.add_task(Task(task_type="Feeding", time_to_complete=10, priority="high", pet=biscuit))
mochi.add_task(Task(task_type="Litter box cleaning", time_to_complete=15, priority="medium", pet=mochi))
mochi.add_task(Task(task_type="Playtime", time_to_complete=20, priority="low", pet=mochi))

schedule = Schedule(owner=owner, time_available=60)
schedule.create_schedule()

print("Today's Schedule")
print("-----------------")
for reason in schedule.explain():
    print(reason)
