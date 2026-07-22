# Command-Line To-Do Application

A simple command-line To-Do application built in Python that helps users manage daily tasks from the terminal. Tasks are stored in a JSON file, allowing them to persist across multiple sessions.

## Features

* Add new tasks
* View all tasks
* Update existing tasks
* Delete tasks
* Mark tasks as completed
* Filter tasks by pending or completed status
* Due date support with overdue indication
* Color-coded terminal output
* JSON-based data persistence

## Technologies Used

* Python
* JSON
* Colorama

## Project Structure

```
TodoCLI/
│── todo.py
│── tasks.json
│── README.md
└── .gitignore
```

## Installation

1. Clone the repository.
2. Install the required package:

```bash
pip install colorama
```

3. Run the application:

```bash
python todo.py
```

## Learning Outcomes

This project helped in understanding:

* File handling in Python
* Working with JSON data
* CRUD operations
* Functions and modular programming
* Building interactive command-line applications
