import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(project_root)
)


import pytest

from student import Student
from student_manager import StudentManager
from file_handler import FileHandler

from exceptions import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
    InvalidStudentDataError
)


@pytest.fixture
def manager(tmp_path):

    manager = StudentManager()

    manager.file_handler = FileHandler(
        str(tmp_path / "students.json")
    )

    manager.students = []

    return manager


def test_add_student(manager):

    student = Student(
        "S101",
        "Ravi",
        21,
        "Python",
        85
    )

    manager.add_student(student)

    assert len(manager.students) == 1

    assert manager.students[0].name == "Ravi"


def test_search_student(manager):

    student = Student(
        "S101",
        "Ravi",
        21,
        "Python",
        85
    )

    manager.add_student(student)

    result = manager.search_student(
        "S101"
    )

    assert result is not None

    assert result.name == "Ravi"


def test_update_student(manager):

    student = Student(
        "S101",
        "Ravi",
        21,
        "Python",
        85
    )

    manager.add_student(student)

    manager.update_student(
        "S101",
        "Ravi Kumar",
        22,
        "Django",
        90
    )

    result = manager.get_student(
        "S101"
    )

    assert result.name == "Ravi Kumar"

    assert result.age == 22

    assert result.course == "Django"

    assert result.marks == 90


def test_delete_student(manager):

    student = Student(
        "S101",
        "Ravi",
        21,
        "Python",
        85
    )

    manager.add_student(student)

    manager.delete_student(
        "S101"
    )

    assert len(manager.students) == 0


def test_duplicate_student_id(manager):

    student1 = Student(
        "S101",
        "Ravi",
        21,
        "Python",
        85
    )

    student2 = Student(
        "S101",
        "Priya",
        22,
        "Java",
        90
    )

    manager.add_student(student1)

    with pytest.raises(
        StudentAlreadyExistsError
    ):

        manager.add_student(student2)


def test_student_not_found(manager):

    with pytest.raises(
        StudentNotFoundError
    ):

        manager.get_student(
            "S999"
        )


def test_invalid_marks(manager):

    student = Student(
        "S101",
        "Ravi",
        21,
        "Python",
        150
    )

    with pytest.raises(
        InvalidStudentDataError
    ):

        manager.add_student(student)