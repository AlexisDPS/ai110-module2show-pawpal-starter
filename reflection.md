# PawPal+ Project Reflection

## 1. System Design

-3 core actions
Add a task
Change task priority
Change constraints

**a. Initial design**

- Briefly describe your initial UML design.
  My initial UML design uses four classes to represent the owner, pet, tasks, and schedule. The classes are connected to organize pet care information and generate a daily plan.
- What classes did you include, and what responsibilities did you assign to each?
  I included four classes: Owner, Pet, Task, and Schedule. The Owner class stores the owner's information. The Pet class stores information about each pet. The Task class stores pet care tasks, including their duration and priority. The Schedule class is responsible for organizing tasks into a daily plan based on the available time.

**b. Design changes**

- Did your design change during implementation?
  Yes
- If yes, describe at least one change and why you made it.
  I added a pets list to the Owner class so multiple pets can be stored by an owner. This matches how I laid out my UML design and will make scheduling easier later on.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
