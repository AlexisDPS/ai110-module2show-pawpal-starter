import streamlit as st

from pawpal_system import Owner, Pet, Task, Schedule

PRIORITY_LABELS = {"high": "🔴 High", "medium": "🟡 Medium", "low": "🟢 Low"}


def priority_label(priority: str) -> str:
    """Return a priority string with a color-coded emoji."""
    return PRIORITY_LABELS.get(priority, priority)


def status_label(is_completed: bool) -> str:
    """Return a status string with a checkmark or hourglass emoji."""
    return "✅ Done" if is_completed else "⏳ Pending"


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")

if "owner" not in st.session_state:
    try:
        st.session_state.owner = Owner.load_from_json()
        st.toast("Loaded saved data from data.json")
    except FileNotFoundError:
        st.session_state.owner = Owner(name=owner_name, age=0)
owner = st.session_state.owner

st.markdown("### Pets")
st.caption("Add pets for this owner.")

col1, col2, col3 = st.columns(3)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    breed = st.text_input("Breed", value="Tabby Cat")
with col3:
    species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    pet = Pet(name=pet_name, age=0, breed=breed, owner=owner)
    owner.add_pet(pet)
    owner.save_to_json()
    st.success(f"🐾 Added {pet_name} ({breed})")

if owner.pets:
    st.write("**Current pets:**")
    st.table([{"Name": p.name, "Breed": p.breed} for p in owner.pets])
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if owner.pets:
    pet_names = [p.name for p in owner.pets]
    selected_pet_name = st.selectbox("Pet", pet_names)
    selected_pet = next(p for p in owner.pets if p.name == selected_pet_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        task = Task(
            task_type=task_title,
            time_to_complete=int(duration),
            priority=priority,
            pet=selected_pet,
        )
        selected_pet.add_task(task)
        owner.save_to_json()
        st.success(f"📝 Added '{task_title}' for {selected_pet.name}")

    all_tasks = owner.get_all_tasks()
    if all_tasks:
        st.write("**Current tasks:**")
        st.table(
            [
                {
                    "Pet": t.pet.name,
                    "Task": t.task_type,
                    "Duration (min)": t.time_to_complete,
                    "Priority": priority_label(t.priority),
                    "Status": status_label(t.is_completed),
                }
                for t in all_tasks
            ]
        )
    else:
        st.info("No tasks yet. Add one above.")
else:
    st.info("Add a pet before adding tasks.")

st.divider()

st.subheader("📅 Build Schedule")
st.caption("Generate today's schedule from the owner's pets and tasks.")

time_available = st.number_input("Time available (minutes)", min_value=1, max_value=1440, value=60)

if st.button("Generate schedule"):
    schedule = Schedule(owner=st.session_state.owner, time_available=int(time_available))
    schedule.create_schedule()

    if schedule.scheduled_tasks:
        st.success(f"✅ Schedule created with {len(schedule.scheduled_tasks)} task(s)!")
        st.table(
            [
                {
                    "Pet": t.pet.name,
                    "Task": t.task_type,
                    "Priority": priority_label(t.priority),
                    "Duration (min)": t.time_to_complete,
                }
                for t in schedule.scheduled_tasks
            ]
        )
    else:
        st.info("No tasks fit in the available time.")

    next_slot = schedule.next_available_slot()
    st.write(f"🕒 **Next available slot:** {next_slot.strftime('%Y-%m-%d %H:%M')}")

    st.markdown("#### ⏱️ Tasks Sorted by Time")
    time_sorted_tasks = schedule.sort_by_time(owner.get_all_tasks())
    if time_sorted_tasks:
        st.table(
            [
                {
                    "Pet": t.pet.name,
                    "Task": t.task_type,
                    "Priority": priority_label(t.priority),
                    "Duration (min)": t.time_to_complete,
                }
                for t in time_sorted_tasks
            ]
        )
    else:
        st.info("No tasks to sort yet.")

    st.markdown("#### 🥇 Tasks Sorted by Priority (then Time)")
    priority_sorted_tasks = schedule.sort_by_priority(owner.get_all_tasks())
    if priority_sorted_tasks:
        st.table(
            [
                {
                    "Pet": t.pet.name,
                    "Task": t.task_type,
                    "Priority": priority_label(t.priority),
                    "Duration (min)": t.time_to_complete,
                }
                for t in priority_sorted_tasks
            ]
        )
    else:
        st.info("No tasks to sort yet.")

    st.markdown("#### ⏳ Pending Tasks")
    pending_tasks = schedule.filter_tasks(is_completed=False)
    if pending_tasks:
        st.table(
            [
                {"Pet": t.pet.name, "Task": t.task_type, "Priority": priority_label(t.priority)}
                for t in pending_tasks
            ]
        )
    else:
        st.info("No pending tasks.")

    st.markdown("#### ⚠️ Scheduling Conflicts")
    conflicts = schedule.find_conflicts()
    if conflicts:
        for warning in conflicts:
            st.warning(warning)
    else:
        st.success("✅ No scheduling conflicts found.")
