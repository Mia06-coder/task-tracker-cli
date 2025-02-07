import datetime, json, re

id_count = 0 # Counter for task IDs
status_list = ["todo", "in-progress", "done"]

while True:
    command = input("task-cli> ").strip()

    # Regular expression to match 'add "description"'
    pattern = r'^add\s+"(.+)"$'  
    match = re.match(pattern, command, re.IGNORECASE)

    if match:
        new_task_description = match.group(1).strip() # Extract task description

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
    elif command.lower() == "help":
        print("\n📌 Available Commands:\n"
              '  - add "task description"  → Add a new task\n'
              "  - help                    → Show available commands\n"
              "  - exit                    → Exit the task tracker\n")
    elif command.lower() == "exit":
        break  # Exit the loop
    elif command == "":
        continue # Ignore empty inputs
    else:
        print(f"❌ '{command}' is not recognised. Type 'help' for valid commands.")
