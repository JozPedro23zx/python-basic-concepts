import json
import os

FILE_PATH = 'data.json'

def saveTask(tasks):
    with open(FILE_PATH, 'w') as f:
        json.dump(tasks, f, indent=4)

def loadTasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def find(title):
    tasks = loadTasks()
    for task in tasks:
        if task['title'] == title:
            return task
    return None

def insert(new_task):
    tasks = loadTasks()
    tasks.append(new_task)
    saveTask(tasks)

def delete(title):
    tasks = loadTasks()
    tasks_updated = [task for task in tasks if task['title'] != title]
    saveTask(tasks_updated)

def update(new_task):
    tasks = loadTasks()
    for i, task in enumerate(tasks):
        if task['title'] == new_task['title']:
            tasks[i] = new_task
            break
    saveTask(tasks)

def findAll():
    return loadTasks()
