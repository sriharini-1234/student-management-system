from student import Student
from file_handler import FileHandler

from exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
    InvalidStudentDataError
)


class StudentManager:

    def __init__(self):
        self.students = []

        self.file_handler = FileHandler(
            "data/students.json"
        )

        self.load_students()

    # Load students from JSON file
    def load_students(self):
        data = self.file_handler.load()

        self.students = []

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )

            self.students.append(student)

    # Save students to JSON file
    def save_students(self):
        self.file_handler.save(self.students)

    # Validate student information
    def validate_student(self, student):

        if not student.student_id.strip():
            raise InvalidStudentDataError(
                "Student ID cannot be empty."
            )

        if not student.name.strip():
            raise InvalidStudentDataError(
                "Student name cannot be empty."
            )

        if student.age < 1 or student.age > 100:
            raise InvalidStudentDataError(
                "Age must be between 1 and 100."
            )

        if not student.course.strip():
            raise InvalidStudentDataError(
                "Course cannot be empty."
            )

        if student.marks < 0 or student.marks > 100:
            raise InvalidStudentDataError(
                "Marks must be between 0 and 100."
            )

    # Add student
    def add_student(self, student):

        self.validate_student(student)

        if self.search_student(student.student_id):
            raise StudentAlreadyExistsError(
                f"Student ID {student.student_id} already exists."
            )

        self.students.append(student)

        self.save_students()

    # Get all students
    def get_all_students(self):
        return self.students

    # Search student
    def search_student(self, student_id):

        for student in self.students:

            if student.student_id.lower() == student_id.lower():
                return student

        return None

    # Get one student
    def get_student(self, student_id):

        student = self.search_student(student_id)

        if student is None:
            raise StudentNotFoundError(
                f"Student ID {student_id} not found."
            )

        return student

    # Update student
    def update_student(
        self,
        student_id,
        name,
        age,
        course,
        marks
    ):

        student = self.get_student(student_id)

        updated_student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        self.validate_student(updated_student)

        student.name = name
        student.age = age
        student.course = course
        student.marks = marks

        self.save_students()

    # Delete student
    def delete_student(self, student_id):

        student = self.get_student(student_id)

        self.students.remove(student)

        self.save_students()
        