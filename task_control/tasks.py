import manage
from datetime import datetime

def addTask():
    title = input("Enter with task title: ").strip()
    if manage.find(title):
        print("A task with this name already exist!")
        return

    description = input("Enter with task description: ").strip()
    priority = input("Enter with task priority (high, normal, low): ").strip().lower()
    deadline = input("Enter with deadline (YYYY-MM-DD): ").strip()

    if priority not in ["high", "normal", "low"]:
        print("Invalid priority, set to 'normal'")
        priority = "normal"

    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date, use the format: YYYY-MM-DD.")
        return

    task = {'title': title, "description": description, "priority": priority, "deadline": deadline}
    manage.insert(task)
    print("Success to add task!")

def deleteTask():
    title = input("Enter with the title task to delete: ").strip()
    if not manage.find(title):
        print("Task not found!")
        return
    manage.delete(title)
    print("Success to delete task!")

def updateTask():
    title = input("Enther with the title task to update: ").strip()
    task = manage.find(title)
    if not task:
        print("Task not found!")
        return

    description = input(f"New description ({task['description']}): ").strip()
    priority = input(f"New priority ({task['priority']}): ").strip().lower()
    deadline = input(f"New deadline ({task['deadline']} - YYYY-MM-DD): ").strip()

    if priority and priority not in ["high", "normal", "low"]:
        print("Invalid priority")
        priority = task['priority']

    try:
        if deadline:
            datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid deadline")
        deadline = task['deadline']

    updated_task = {
        'title': title,
        'description': description if description else task['description'],
        'priority': priority if priority else task['priority'],
        'deadline': deadline if deadline else task['deadline']
    }

    manage.update(updated_task)
    print("Success to update task")

def listTask():
    tasks = manage.findAll()
    if not tasks:
        print("Not found any task")
    else:
        print("Tasks found:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - Priority: {task['priority']}, Deadline: {task['deadline']}")
            print(f"Description:\n{task['description']}\n")

def calculate_days():
    title = input("Task title: ").strip()
    task = manage.find(title)

    if task is None:
        print("Task not found.")
        return
    
    deadline_str = task.get('deadline')
    if not deadline_str:
        print("The task does not have a defined deadline.")
        return

    try:
        deadline_date = datetime.strptime(deadline_str, '%Y-%m-%d').date()
        today = datetime.today().date()
        
        days_left = (deadline_date - today).days
        
        if days_left > 0:
            print(f"{days_left} days left until the task deadline '{title}'.")
        elif days_left == 0:
            print(f"The deadline of the task '{title}' is today!")
        else:
            print(f"The task '{title}' is already overdue by {-days_left} days.")
    except ValueError:
        print("Invalid date, use the format: YYYY-MM-DD.")