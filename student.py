import json
import os

DATA_FILE = "student_data.json"


class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data["email"]
        )


def load_students():
    """Load students from JSON file."""

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return [Student.from_dict(student) for student in data]

    except json.JSONDecodeError:
        print("Error: Invalid JSON data.")
        return []


def save_students(students):
    """Save students to JSON file."""

    with open(DATA_FILE, "w") as file:
        json.dump(
            [student.to_dict() for student in students],
            file,
            indent=4
        )


def generate_student_id(students):
    """Generate the next student ID."""

    if not students:
        return 1

    return max(student.student_id for student in students) + 1


def add_student(name, age, course, email):
    """Add a new student."""

    students = load_students()

    student_id = generate_student_id(students)

    student = Student(
        student_id,
        name,
        age,
        course,
        email
    )

    students.append(student)

    save_students(students)

    return student


def get_all_students():
    """Return all students."""

    return load_students()


def find_student(student_id):
    """Find a student by ID."""

    students = load_students()

    for student in students:
        if student.student_id == student_id:
            return student

    return None


def update_student(student_id, name, age, course, email):
    """Update an existing student."""

    students = load_students()

    for student in students:

        if student.student_id == student_id:

            student.name = name
            student.age = age
            student.course = course
            student.email = email

            save_students(students)

            return True

    return False


def delete_student(student_id):
    """Delete a student."""

    students = load_students()

    for student in students:

        if student.student_id == student_id:

            students.remove(student)

            save_students(students)

            return True

    return False