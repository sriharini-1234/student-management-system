from student import Student
from student_manager import StudentManager
from exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
    InvalidStudentDataError
)


def display_menu():
    print("\n" + "=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)


def add_student(manager):
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Name: ").strip()

    try:
        age = int(input("Enter Age: "))
        course = input("Enter Course: ").strip()
        marks = float(input("Enter Marks: "))

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        manager.add_student(student)

        print("\nStudent added successfully!")

    except ValueError:
        print("\nInvalid input.")
        print("Age must be a number.")
        print("Marks must be a number.")

    except (
        StudentAlreadyExistsError,
        InvalidStudentDataError
    ) as error:
        print(f"\nError: {error}")


def view_students(manager):
    print("\n--- All Students ---")

    students = manager.get_all_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        student.display()
        print("-" * 30)


def search_student(manager):
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ").strip()

    try:
        student = manager.get_student(student_id)

        print("\nStudent Found")
        print("-" * 30)

        student.display()

    except StudentNotFoundError as error:
        print(f"\nError: {error}")


def update_student(manager):
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ").strip()

    try:
        manager.get_student(student_id)

        name = input("Enter New Name: ").strip()
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ").strip()
        marks = float(input("Enter New Marks: "))

        manager.update_student(
            student_id,
            name,
            age,
            course,
            marks
        )

        print("\nStudent updated successfully!")

    except ValueError:
        print("\nInvalid input.")
        print("Age must be a number.")
        print("Marks must be a number.")

    except (
        StudentNotFoundError,
        InvalidStudentDataError
    ) as error:
        print(f"\nError: {error}")


def delete_student(manager):
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ").strip()

    try:
        student = manager.get_student(student_id)

        print("\nStudent Details")
        print("-" * 30)

        student.display()

        confirmation = input(
            "\nAre you sure you want to delete this student? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            manager.delete_student(student_id)
            print("\nStudent deleted successfully!")
        else:
            print("\nDelete operation cancelled.")

    except StudentNotFoundError as error:
        print(f"\nError: {error}")


def main():
    manager = StudentManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(manager)

        elif choice == "2":
            view_students(manager)

        elif choice == "3":
            search_student(manager)

        elif choice == "4":
            update_student(manager)

        elif choice == "5":
            delete_student(manager)

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()