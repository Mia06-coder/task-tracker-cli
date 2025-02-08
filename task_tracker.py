import datetime, json, re, os

class TaskTracker():
    def __init__(self):    
        self.json_file = "tasks.json"
        self.id_count = 0 # Counter for task IDs
        self.status_list = ["todo", "in-progress", "done"]

    def readJson(self):
        try:
            if not os.path.exists(self.json_file):  # Check if file exists
                return []
            with open(self.json_file, "r") as file:
                tasks = json.load(file)
                return tasks
        except json.JSONDecodeError:  # Handle invalid JSON format
            print("⚠️ Error: Corrupted JSON file. Starting fresh.")
            return []

    def addTask(self, match):
        new_task_description = match.group(1).strip() # Extract task description
        tasks = self.readJson()

        # Check for duplicate tasks
        if any(task["description"].lower() == new_task_description.lower() for task in tasks):
            print("❌ Task already exists!")
            return
        
        last_id = tasks[-1]["id"] if tasks else 0  # Get last ID
        new_task_id = last_id + 1 # Assign new ID

        # Get current date and time
        current_date = datetime.datetime.now()
        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        formatted_date = f"{current_date.day}-{months[current_date.month - 1]}-{current_date.year}"
        formatted_time = f" {str(current_date.hour).zfill(2)}:{str(current_date.minute).zfill(2)}:{str(current_date.second).zfill(2)}"

        new_task = {
            "id":new_task_id,
            "description": new_task_description,
            "status": self.status_list[0],
            "createdAt": f"{formatted_date} {formatted_time}"
        }

        # Append new task
        tasks.append(new_task)

        with open(self.json_file, "w") as file: 
            json.dump(tasks, file, indent=4, separators=(",",":"))
        
        print(f"Task added successfully (ID:{new_task_id})")

    def listTasks(self):
        task_list = self.readJson()

        if not task_list:
            print("No tasks available.")
            return
        
        print("\n📋 Your Tasks\n" + "=" * 75)
        print(f"{'ID':<5}{'Description':<30}  {'Status':<15}  {'Created At'}")
        print("-" * 75)
    
        for task in task_list:
            id = task["id"]
            desc = (task["description"][:27] + '...') if len(task["description"]) > 30 else task["description"]
            status = task["status"]
            created = task["createdAt"]

            print(f"{id:<5}{desc:<30}  {status:<15}  {created}")
        
        print("=" * 75)

    def displayCommands(self):
        print("\n📌 Available Commands:\n"
              '  - add "task description"  → Add a new task\n'
              "  - list                    → List all tasks\n"
              "  - help                    → Show available commands\n"
              "  - exit                    → Exit the task tracker\n")

task_tracker = TaskTracker()

while True:
    command = input("task-cli> ").strip()

    # Regular expression to match 'add "description"'
    add_task_pattern = r'^add\s+"(.+)"$'  
    add_task_match = re.match(add_task_pattern, command, re.IGNORECASE)

    if add_task_match:
        task_tracker.addTask(add_task_match)
    elif command.lower() == "list":
        task_tracker.listTasks()
    elif command.lower() == "help":
        task_tracker.displayCommands()
    elif command.lower() == "exit":
        break  # Exit the loop
    elif command == "":
        continue # Ignore empty inputs
    else:
        print(f"❌ '{command}' is not recognised. Type 'help' for valid commands.")
