import json
import os

FILE = "students.json"

# Load students from file
def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save students to file
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

students = load_students()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter ID: ")

        # Check unique ID
        found = False
        for s in students:
            if s["id"] == sid:
                found = True
                break

        if found:
            print("ID already exists!")
        else:
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")

            student = {
                "id": sid,
                "name": name,
                "grade": grade
            }

            students.append(student)
            save_students(students)
            print("Student Added!")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nID\tName\t\tGrade")
            print("-" * 30)
            for s in students:
                print(f"{s['id']}\t{s['name']}\t\t{s['grade']}")

    elif choice == "3":
        sid = input("Enter ID to delete: ")

        for s in students:
            if s["id"] == sid:
                students.remove(s)
                save_students(students)
                print("Student Deleted!")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")