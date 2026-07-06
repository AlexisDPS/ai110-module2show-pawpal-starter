from pawpal_system import Owner, Pet, Task


def test_mark_complete_changes_status():
    owner = Owner(name="Jordan", age=30)
    pet = Pet(name="Biscuit", age=3, breed="Golden Retriever", owner=owner)
    task = Task(task_type="Morning walk", time_to_complete=30, priority="high", pet=pet)

    assert task.is_completed is False

    task.mark_complete()

    assert task.is_completed is True


def test_add_task_increases_pet_task_count():
    owner = Owner(name="Jordan", age=30)
    pet = Pet(name="Biscuit", age=3, breed="Golden Retriever", owner=owner)
    task = Task(task_type="Feeding", time_to_complete=10, priority="high", pet=pet)

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
