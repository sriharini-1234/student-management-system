# from student import Student
# from student_manager import StudentManager
# from exceptions import (
#     StudentAlreadyExistsError,
#     StudentNotFoundError,
#     InvalidStudentDataError
# )


# def display_menu():
#     print("\n" + "=" * 45)
#     print("       STUDENT MANAGEMENT SYSTEM")
#     print("=" * 45)
#     print("1. Add Student")
#     print("2. View All Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Exit")
#     print("=" * 45)


# def add_student(manager):
#     print("\n--- Add Student ---")

#     student_id = input("Enter Student ID: ").strip()
#     name = input("Enter Name: ").strip()

#     try:
#         age = int(input("Enter Age: "))
#         course = input("Enter Course: ").strip()
#         marks = float(input("Enter Marks: "))

#         student = Student(
#             student_id,
#             name,
#             age,
#             course,
#             marks
#         )

#         manager.add_student(student)

#         print("\nStudent added successfully!")

#     except ValueError:
#         print("\nInvalid input.")
#         print("Age must be a number.")
#         print("Marks must be a number.")

#     except (
#         StudentAlreadyExistsError,
#         InvalidStudentDataError
#     ) as error:
#         print(f"\nError: {error}")


# def view_students(manager):
#     print("\n--- All Students ---")

#     students = manager.get_all_students()

#     if not students:
#         print("No students found.")
#         return

#     for student in students:
#         student.display()
#         print("-" * 30)


# def search_student(manager):
#     print("\n--- Search Student ---")

#     student_id = input("Enter Student ID: ").strip()

#     try:
#         student = manager.get_student(student_id)

#         print("\nStudent Found")
#         print("-" * 30)

#         student.display()

#     except StudentNotFoundError as error:
#         print(f"\nError: {error}")


# def update_student(manager):
#     print("\n--- Update Student ---")

#     student_id = input("Enter Student ID: ").strip()

#     try:
#         manager.get_student(student_id)

#         name = input("Enter New Name: ").strip()
#         age = int(input("Enter New Age: "))
#         course = input("Enter New Course: ").strip()
#         marks = float(input("Enter New Marks: "))

#         manager.update_student(
#             student_id,
#             name,
#             age,
#             course,
#             marks
#         )

#         print("\nStudent updated successfully!")

#     except ValueError:
#         print("\nInvalid input.")
#         print("Age must be a number.")
#         print("Marks must be a number.")

#     except (
#         StudentNotFoundError,
#         InvalidStudentDataError
#     ) as error:
#         print(f"\nError: {error}")


# def delete_student(manager):
#     print("\n--- Delete Student ---")

#     student_id = input("Enter Student ID: ").strip()

#     try:
#         student = manager.get_student(student_id)

#         print("\nStudent Details")
#         print("-" * 30)

#         student.display()

#         confirmation = input(
#             "\nAre you sure you want to delete this student? (y/n): "
#         ).strip().lower()

#         if confirmation == "y":
#             manager.delete_student(student_id)
#             print("\nStudent deleted successfully!")
#         else:
#             print("\nDelete operation cancelled.")

#     except StudentNotFoundError as error:
#         print(f"\nError: {error}")


# def main():
#     manager = StudentManager()

#     while True:
#         display_menu()

#         choice = input("Enter your choice: ").strip()

#         if choice == "1":
#             add_student(manager)

#         elif choice == "2":
#             view_students(manager)

#         elif choice == "3":
#             search_student(manager)

#         elif choice == "4":
#             update_student(manager)

#         elif choice == "5":
#             delete_student(manager)

#         elif choice == "6":
#             print("\nThank you for using Student Management System!")
#             break

#         else:
#             print("\nInvalid choice.")
#             print("Please enter a number from 1 to 6.")


# if __name__ == "__main__":
#     main()
from student import (
    add_student,
    get_all_students,
    find_student,
    update_student,
    delete_student
)


def display_menu():
    print("\n" + "=" * 50)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    print("=" * 50)


def get_valid_age():
    """Get a valid age from the user."""

    while True:

        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            if age > 100:
                print("Please enter a valid age.")
                continue

            return age

        except ValueError:
            print("Please enter a number.")


def get_valid_email():
    """Get a valid email."""

    while True:

        email = input("Enter email: ").strip()

        if "@" in email and "." in email:
            return email

        print("Please enter a valid email.")


def add_student_menu():
    """Get student details and add student."""

    print("\n--- ADD STUDENT ---")

    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age = get_valid_age()

    course = input("Enter course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    email = get_valid_email()

    student = add_student(
        name,
        age,
        course,
        email
    )

    print("\nStudent added successfully!")
    print(f"Student ID: {student.student_id}")


def view_students():
    """Display all students."""

    print("\n--- ALL STUDENTS ---")

    students = get_all_students()

    if not students:
        print("No students found.")
        return

    print("-" * 85)

    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Course':<20}"
        f"{'Email':<30}"
    )

    print("-" * 85)

    for student in students:

        print(
            f"{student.student_id:<5}"
            f"{student.name:<20}"
            f"{student.age:<8}"
            f"{student.course:<20}"
            f"{student.email:<30}"
        )

    print("-" * 85)


def search_student():
    """Search for a student."""

    print("\n--- SEARCH STUDENT ---")

    try:
        student_id = int(input("Enter student ID: "))

        student = find_student(student_id)

        if student is None:
            print("Student not found.")
            return

        print("\nStudent Details")
        print("-" * 30)

        print(f"ID     : {student.student_id}")
        print(f"Name   : {student.name}")
        print(f"Age    : {student.age}")
        print(f"Course : {student.course}")
        print(f"Email  : {student.email}")

    except ValueError:
        print("Please enter a valid student ID.")


def update_student_menu():
    """Update student information."""

    print("\n--- UPDATE STUDENT ---")

    try:
        student_id = int(input("Enter student ID: "))

        student = find_student(student_id)

        if student is None:
            print("Student not found.")
            return

        print("\nEnter new information.")

        name = input("Enter name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        age = get_valid_age()

        course = input("Enter course: ").strip()

        if not course:
            print("Course cannot be empty.")
            return

        email = get_valid_email()

        success = update_student(
            student_id,
            name,
            age,
            course,
            email
        )

        if success:
            print("Student updated successfully.")

    except ValueError:
        print("Please enter a valid student ID.")


def delete_student_menu():
    """Delete a student."""

    print("\n--- DELETE STUDENT ---")

    try:
        student_id = int(input("Enter student ID: "))

        student = find_student(student_id)

        if student is None:
            print("Student not found.")
            return

        print(f"Student Name: {student.name}")

        confirmation = input(
            "Are you sure you want to delete? (y/n): "
        ).lower()

        if confirmation == "y":

            success = delete_student(student_id)

            if success:
                print("Student deleted successfully.")

        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Please enter a valid student ID.")


def main():
    """Main application."""

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student_menu()

        elif choice == "5":
            delete_student_menu()

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()