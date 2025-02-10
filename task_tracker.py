import datetime, json, re, os

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    
class TaskTracker():
    def __init__(self):    
        self.json_file = "tasks.json"
        self.id_count = 0 # Counter for task IDs
        self.status_list = ["todo", "in-progress", "done"]

    def currentDateTime(self):
        """
        Formats date and time to d-MMM-YYYY HH:MM.
        """
        # Get current date and time
        current_date = datetime.datetime.now()
        self.formatted_date = f"{current_date.day}-{MONTHS[current_date.month - 1]}-{current_date.year}"
        self.formatted_time = f" {str(current_date.hour).zfill(2)}:{str(current_date.minute).zfill(2)}"

    def readJson(self):
        """
        Reads the JSON file and returns the list of tasks.
        
        Returns:
            List[Dict[str, str]]: A list of tasks, where each task is represented as a dictionary.
        """
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
        """
        Writes the given list of tasks back to the JSON file.
        
        Args:
            tasks (List[Dict[str, str]]): The list of tasks to write to the file.
        """
        try:
            with open(self.json_file, "w") as file: 
                json.dump(tasks, file, indent=4, separators=(",",":"))
        except IOError as e:
            print(f"⚠️ Error writing to file: {e}")
            
    def addTask(self, match):
        """
        Adds a new task with a default status of "todo".
        
        Args:
            match (Match[str]): The regex match object containing the task description.
        """
        new_task_description = match.group(1).strip() # Extract task description
        tasks = self.readJson()

        # Check for duplicate tasks
        if any(task["description"].lower() == new_task_description.lower() for task in tasks):
            print("❌ Task already exists!")
            return
        
        new_task_id = max((task["id"] for task in tasks), default=0) + 1


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

    def updateTask(self, match):     
        """
        AUpdates an existing task.
        
        Args:
            match (Match[str]): The regex match object containing the new task description.
        """
        task_id = match.group(1).strip()
        new_task_description = match.group(2).strip()
        print(new_task_description)
        task_list = self.readJson()
        self.found = False

        for task in task_list:
            if task["id"] == int(task_id):
                self.found = True

                self.currentDateTime()
                task["description"] = new_task_description
                task["updatedAt"] = f"{self.formatted_date} {self.formatted_time}"
                self.writeJson(task_list)
                print(f"Task (ID:{task_id}) successfully updated")
                break
            
        if not self.found:
            print(f"Task (ID:{task_id}) not found!")
            
    def deleteTask(self, match):
        """
        Deletes a task from the list based on its ID.
        
        Args:
            match (Match[str]): The regex match object containing the task ID.
        """
        task_id = match.group(1).strip()
        task_list = self.readJson()

        if not task_list:
            print("No tasks available.")
            return
        
        self.found = False
        task_to_remove = None
        
        # Find the task to delete
        for index, task in enumerate(task_list):
            if task["id"] == int(task_id):
                task_to_remove = task
                self.found = True
                break

        if self.found:
            task_list.remove(task_to_remove)
            self.writeJson(task_list)
            print(f"Task (ID:{task_id}) successfully deleted!")
        else:
            print(f"Task (ID:{task_id}) not found!")

    def displayTasks(self, task_list):
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

    def listTasks(self):
        """
        Lists all tasks, displaying their ID, description, status, and timestamps.
        """
        task_list = self.readJson()

        if not task_list:
            print("No tasks available.")
            return
        
        self.displayTasks(task_list)

    def listByStatus(self, match):
        """
        Lists tasks filtered by their status.
        
        Args:
            match (Match[str]): The regex match object containing the status to filter by.
        """
        task_status = match.group(1).strip().lower()
        task_list = self.readJson()

        if not task_list:
            print("No tasks available.")
            return
        
        filtered_tasks = [task for task in task_list 
                          if task["status"].lower() == task_status]
        
        if not filtered_tasks:
            print(f"No tasks found with status: '{task_status}'")
            return
        
        self.displayTasks(filtered_tasks)

    def markStatus(self, match, status): 
        """
        Updates the status of a task (e.g., "in-progress" or "done").
        
        Args:
            match (Match[str]): The regex match object containing the task ID.
            status (str): The new status to set for the task.
        """    
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
        """
        Lists all commands of the Task Tracker CLI.
        """
        print("\n📌 Available Commands:\n"
              '  - add "task description"               → Add a new task\n'
              '  - update <task_id> "task description"  → Updates an existing task\n'
              "  - list                                 → List all tasks\n"
              "  - list <status>                        → List tasks by status (done, todo, in-progress)\n"
              "  - mark-<status> <task_id>              → Mark task as done or in-progress\n"
              "  - help                                 → Show available commands\n"
              "  - exit                                 → Exit the task tracker\n")

task_tracker = TaskTracker()

while True:
    command = input("task-cli> ").strip()

    # Regular expression to match 'add "description"'
    add_task_pattern = r'^add\s+"(.+)"$'  
    add_task_match = re.match(add_task_pattern, command, re.IGNORECASE)
    
    update_task_pattern = r'^update\s+(\d+)\s+"(.+)"$'
    update_task_match = re.match(update_task_pattern, command, re.IGNORECASE)

    mark_in_progress_pattern = r'^mark-in-progress\s+(\d+)$'
    mark_in_progress_match = re.match(mark_in_progress_pattern, command, re.IGNORECASE)

    mark_done_pattern = r'^mark-done\s+(\d+)$'
    mark_done_match = re.match(mark_done_pattern, command, re.IGNORECASE)

    list_by_status_pattern = r'^list\s+(done|todo|in-progress)$'
    list_by_status_match = re.match(list_by_status_pattern, command, re.IGNORECASE)

    delete_pattern = r'^delete\s+(\d+)$'
    delete_match = re.match(delete_pattern, command, re.IGNORECASE)

    if add_task_match:
        task_tracker.addTask(add_task_match)
    elif update_task_match:
        task_tracker.updateTask(update_task_match)
    elif mark_in_progress_match:
        task_tracker.markStatus(mark_in_progress_match, task_tracker.status_list[1])
    elif mark_done_match:
        task_tracker.markStatus(mark_done_match, task_tracker.status_list[2])
    elif list_by_status_match:
        task_tracker.listByStatus(list_by_status_match)
    elif delete_match:
        task_tracker.deleteTask(delete_match)
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
