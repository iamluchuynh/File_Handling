import os
import json
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    '''
    Show all task
    task = {
        "id": 
        "title": 
        "category": 
        "description":
        "add_date"
        "due_date": 
        "finished_date": 
        "completed": 
    }
    '''
    # TODO: Fill here
    ...
    ...
    

def list_tasks(tasks):
    '''
    Show all task
    '''
    # TODO: Fill here
    ...
    ...

def mark_task_completed(tasks):
    '''
    Change state of the task to complete and add finish date
    '''
    task_id = int(input("Enter the ID of the task to mark as completed: "))
    # TODO: Fill here
    ...
    ...

def delete_task(tasks):
    '''
    Delete a task
    '''
    task_id = int(input("Enter the ID of the task to delete: "))
    # TODO: Fill here
    ...
    ...

def search_tasks(tasks):
    '''
    Find task by keyword, check the keyword is inside description, title or id 
    '''
    keyword = input("Enter a keyword to search for: ").lower()
    # TODO: Fill here
    ...
    ...