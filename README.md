# 📝 Task Tracker CLI

A simple **Command Line Interface (CLI) Task Tracker** that helps you **add, track, and manage tasks** efficiently. This project is designed to **improve programming skills** by working with file handling, user inputs, and interactive CLI applications.

## 🚀 Features

- ✅ Add new tasks via the CLI
- 📌 Track tasks with statuses: `todo`, `in-progress`, `done`
- 💾 Store tasks in JSON format for persistence
- 🕒 Timestamp tasks when added
- 🎯 Simple and lightweight

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

## Usage

- **Add a new task**

  ```sh
  task-cli> add "Your Task Description"
  ```

  Example:

  ```sh
  task-cli> add "Complete the project report"
  ```

- **View tasks**

  ```sh
  task-cli> list
  ```

  Output:

  ```sh
  📋 Your Tasks
   ===========================================================================
   ID   Description                     Status           Created At
   ---------------------------------------------------------------------------
   1    Task Description                status           d-MMM-YYYY  HH:MM:SS
   2    Task Description                status           d-MMM-YYYY  HH:MM:SS
   ===========================================================================
  ```

- **Update task status**

  ```sh
  task-cli> mark-in-progress 2
  Task (ID:2) already 'in-progress'
  task-cli> mark-done 3
  Task (ID:3) successfully marked as 'done'
  task-cli> mark-done 30
  Task (ID:30) not found!
  ```

  ```sh
  ==================================================================================================
  ID   Description                     Status           Created At             Updated At
  --------------------------------------------------------------------------------------------------
  1    Complete the project report     todo             7-FEB-2025  22:13:28
  2    Move to next stage in project   in-progress      7-FEB-2025  22:13:59   9-FEB-2025  16:46:59
  3    Go for a run                    done             7-FEB-2025  22:20:00   9-FEB-2025  17:22:39
  ```

## 🛠️ Technologies Used

- **Python** (for core logic)
- **JSON** (for storing tasks)

## 🏗️ Future Enhancements

- 📝 List all tasks
- 🔄 Update task status
- ❌ Delete a task
