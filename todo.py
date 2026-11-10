tasks = []

def add_task(task):
    tasks.append(task)
    return tasks

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    return tasks

def list_tasks():
    return tasks
# Feature: list tasks
