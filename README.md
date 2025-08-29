# Task Manager CLI

A simple **command-line task manager** built with **Python, SQLite, SQLAlchemy, and Alembic**.
It lets you add, view, update, and delete tasks easily from your terminal.

---

## Features

- Add a task with a title (status defaults to **Pending**)
- View all tasks in a clean table format
- Update the status of a task (**Pending → In Progress → Completed**)
- Delete tasks you no longer need
- Data is stored in a **SQLite database (`tasks.db`)**
- Migrations handled with **Alembic**

---

## Project Structure

task_manager/
│── alembic/ # Migration scripts
│── cli.py # Main CLI program
│── database.py # Database connection (SessionLocal, engine, Base)
│── models.py # Task model definition
│── alembic.ini # Alembic configuration
│── tasks.db # SQLite database file (auto-created after migrations)

## How It Works
- The database is stored in a file called tasks.db in the project folder.

- models.py defines the Task table (id, title, status).

- cli.py handles all user interactions.

- Alembic manages database migrations (so you can modify the schema later).

## Future Improvements

- Filter tasks by status (e.g., show only "Completed" tasks)

- Add due dates and priorities

## Usage

- Start the CLI:
- ```bash
- python cli.py

## Example Run
Choose an option: 1
Enter task title: Buy groceries
Task added with ID 1.

Choose an option: 2
ID   Title                         Status
--------------------------------------------------
1    Buy groceries                 Pending



