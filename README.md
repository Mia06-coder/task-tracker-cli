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

- **Update task status** (Feature in progress 🚧)

## 🛠️ Technologies Used

- **Python** (for core logic)
- **JSON** (for storing tasks)

## 🏗️ Future Enhancements

- 📝 List all tasks
- 🔄 Update task status
- ❌ Delete a task
