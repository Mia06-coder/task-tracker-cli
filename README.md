# 📝 Task Tracker CLI

A simple **Command Line Interface (CLI) Task Tracker** that helps you **add, track, and manage tasks** efficiently. This project is designed to **improve programming skills** by working with file handling, user inputs, and interactive CLI applications.

## 🚀 Features

- ✅ Add new tasks via the CLI
- 📌 Track tasks with statuses: `todo`, `in-progress`, `done`
- 💾 Store tasks in JSON format for persistence
- 🕒 Timestamps for task creation and updates
- 📋 Filter tasks by statu
- 🎯 Lightweight & Simple to use

## 📦 Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Mia06-coder/task-tracker-cli.git
   cd task-tracker-cli
   ```
2. **Run the script**
   ```sh
   python task_tracker.py
   ```

## 🎯 Usage

### 📌 Available Commands

```sh
Command                               Description
add "task description"                Add a new task
update <task_id> "new description"    Update an existing task
list                                  List all tasks
list <status>                         List tasks by status (done, todo, in-progress)
mark-done <task_id>                   Mark a task as done
mark-in-progress <task_id>            Mark a task as in-progress
delete <task_id>                      Delete a task
help                                  Show available commands
exit                                  Exit the task tracker
```

### 🔄 Task Management Examples

- **📌 Add a new task**

  ```sh
  task-cli> add "Complete the project report"
  ```

- **✏️ Update a Task**

  ```sh
  task-cli> update 1 "Submit the final project report"
  ```

- **📋 List tasks**

  ```sh
  task-cli> list
  ```

  Example Output:

  ```sh
  📋 Your Tasks
  ==================================================================================================
  ID   Description                     Status           Created At             Updated At
  --------------------------------------------------------------------------------------------------
  1    Complete the project report     todo             7-FEB-2025  22:13:28
  2    Move to next stage in project   in-progress      7-FEB-2025  22:13:59   9-FEB-2025  16:46:59
  3    Go for a run                    done             7-FEB-2025  22:20:00   9-FEB-2025  17:22:39
  ==================================================================================================
  ```

- **📌 List Tasks by Status**

  ```sh
  task-cli> list done
  ```

- **🔄 Update task status**

  ```sh
  task-cli> mark-in-progress 2
  task-cli> mark-done 3
  ```

- **❌ Delete a task**

  ```sh
  task-cli> delete 1
  ```

  Example Output:

  ```sh
  Task (ID:1) successfully deleted!
  ```

- **ℹ️ View Available Commands**

  ```sh
  task-cli> help
  ```

- **🚪 Exit the CLI**

  ```sh
  task-cli> exit
  ```

## 🛠️ Technologies Used

- **Python** (for core logic)
- **JSON** (for storing tasks)

## 🏗️ Future Enhancements

- 📌 Search & filter tasks
- 📅 Set due dates & reminders
- 🏷️ Tag tasks by category
- 📊 Generate task reports

## 🎨 Credits & Inspiration

This project idea was inspired by [roadmap.sh](https://roadmap.sh/projects/task-tracker).  
Check it out for more project ideas and learning resources!
