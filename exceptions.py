class StudentManagementError(Exception):
    """Base exception for student management system."""
    pass


class StudentAlreadyExistsError(StudentManagementError):
    """Raised when student ID already exists."""
    pass


class StudentNotFoundError(StudentManagementError):
    """Raised when student is not found."""
    pass


class InvalidStudentDataError(StudentManagementError):
    """Raised when student data is invalid."""
    pass