# Student Management System

## Overview

The Student Management System is a simple Command Line Interface (CLI) application developed in Python. It allows users to manage student records efficiently by adding, viewing, and deleting student information. The application stores data permanently using a JSON file.

## Features

* Add new student records
* View all student records
* Delete existing student records
* Validate unique student IDs
* Store data permanently using JSON file
* Simple and user-friendly CLI interface

## Technologies Used

* Python 3
* JSON (for data storage)

## Project Structure

```
Student-Management-System/
│
├── Main.py
├── students.json
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone <your-github-repository-link>
```

2. Navigate to the project directory:

```bash
cd Student-Management-System
```

3. Run the Python file:

```bash
python student_management.py
```

## Sample Menu

```
--- Student Management System ---
1. Add Student
2. Show Students
3. Delete Student
4. Exit
```

## Data Storage

All student records are stored in a `students.json` file in the following format:

```json
[
    {
        "id": "101",
        "name": "Gunjan Kumar",
        "grade": "A"
    }
]
```

## Future Enhancements

* Update student records
* Search students by ID
* Sort student records
* Add graphical user interface (GUI)

## Author

**Gunjan Kumar Sah**

## License

This project is open-source and available for educational purposes.
