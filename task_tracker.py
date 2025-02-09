import datetime, json, re, os

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    
class TaskTracker():
    def __init__(self):    
        self.json_file = "tasks.json"
        self.id_count = 0 # Counter for task IDs
        self.status_list = ["todo", "in-progress", "done"]

    def currentDateTime(self):
        # Get current date and time
        current_date = datetime.datetime.now()
        self.formatted_date = f"{current_date.day}-{MONTHS[current_date.month - 1]}-{current_date.year}"
        self.formatted_time = f" {str(current_date.hour).zfill(2)}:{str(current_date.minute).zfill(2)}"

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

    def writeJson(self, tasks):
        try:
            with open(self.json_file, "w") as file: 
                json.dump(tasks, file, indent=4, separators=(",",":"))
        except json.JSONDecodeError:  # Handle invalid JSON format
            print("⚠️ Error: Corrupted JSON file. Starting fresh.")

    def addTask(self, match):
        new_task_description = match.group(1).strip() # Extract task description
        tasks = self.readJson()

        # Check for duplicate tasks
        if any(task["description"].lower() == new_task_description.lower() for task in tasks):
            print("❌ Task already exists!")
            return
        
        last_id = tasks[-1]["id"] if tasks else 0  # Get last ID
        new_task_id = last_id + 1 # Assign new ID

        self.currentDateTime()
        
        new_task = {
            "id":new_task_id,
            "description": new_task_description,
            "status": self.status_list[0],
            "createdAt": f"{self.formatted_date} {self.formatted_time}"
        }

        # Append new task
        tasks.append(new_task)
        self.writeJson(tasks)
        
        print(f"Task added successfully (ID:{new_task_id})")

    def listTasks(self):
        task_list = self.readJson()

        if not task_list:
            print("No tasks available.")
            return
        
        print("\n📋 Your Tasks\n" + "=" * 98)
        print(f"{'ID':<5}{'Description':<30}  {'Status':<15}  {'Created At':<21}  {'Updated At'}")
        print("-" * 98)
    
        for task in task_list:
            id = task["id"]
            desc = (task["description"][:27] + '...') if len(task["description"]) > 30 else task["description"]
            status = task["status"]
            created = task["createdAt"]
            updated = task.get("updatedAt", "")

            print(f"{id:<5}{desc:<30}  {status:<15}  {created:<21}  {updated}")
        
        print("=" * 98)

    def markStatus(self, match, status):     
        task_id = match.group(1).strip()
        task_list = self.readJson()
        self.found = False

        for task in task_list:
            if task["id"] == int(task_id):
                self.found = True

                if task["status"] != status:
                    self.currentDateTime()

                    task["status"] = status
                    task["updatedAt"] = f"{self.formatted_date} {self.formatted_time}"

                    self.writeJson(task_list)
                    print(f"Task (ID:{task_id}) successfully marked as '{status}'")
                    break
                else:
                    print(f"Task (ID:{task_id}) already '{status}'")
                    break
            
        if not self.found:
            print(f"Task (ID:{task_id}) not found!")
            
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

    mark_in_progress_pattern = r'^mark-in-progress\s+(\d+)$'
    mark_in_progress_match = re.match(mark_in_progress_pattern, command, re.IGNORECASE)

    mark_done_pattern = r'^mark-done\s+(\d+)$'
    mark_done_match = re.match(mark_done_pattern, command, re.IGNORECASE)

    if add_task_match:
        task_tracker.addTask(add_task_match)
    elif mark_in_progress_match:
        task_tracker.markStatus(mark_in_progress_match, task_tracker.status_list[1])
    elif mark_done_match:
        task_tracker.markStatus(mark_done_match, task_tracker.status_list[2])
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
