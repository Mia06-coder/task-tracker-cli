import datetime
import json

id_count = 0 # Counter for task IDs
status_list = ["todo", "in-progress", "done"]
command = input("task-cli> ")

if command.startswith("add "):
    new_task_description = command[4:].strip().strip('"')# Trim "add " and extra spaces

    # Load existing tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            last_id = tasks[-1]["id"] if tasks else 0  # Get last ID
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
        last_id = 0

    new_task_id = last_id + 1 # Assign new ID

    # Get current date and time
    current_date = datetime.datetime.now()
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    formatted_date = f"{current_date.day}-{months[current_date.month - 1]}-{current_date.year}"
    formatted_time = f" {str(current_date.hour).zfill(2)}:{str(current_date.minute).zfill(2)}:{str(current_date.second).zfill(2)}"

    new_task = {
        "id":new_task_id,
        "description": new_task_description,
        "status": status_list[0],
        "createdAt": f"{formatted_date} {formatted_time}"
    }

    # Append new task
    tasks.append(new_task)

    with open("tasks.json", "w") as file: 
        json.dump(tasks, file, indent=4, separators=(",",":"))
    
    print("Task added successfully!")
else:
    print(f"{command} is not recognized as a command")
