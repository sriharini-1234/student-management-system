# Student Management System

A beginner-friendly Python-based Student Management System for managing student records using Object-Oriented Programming, JSON file handling, CRUD operations, input validation, and exception handling.

---

## Project Overview

The Student Management System is a console-based Python application that allows users to manage student records.

The application provides the following operations:

- Add a student
- View all students
- Search for a student
- Update student details
- Delete a student
- Store student data permanently in a JSON file

This project was developed to understand how Python concepts can be combined to build a complete real-world application.

---

## Project Objectives

The main objectives of this project are:

- To understand Python fundamentals
- To implement Object-Oriented Programming
- To use functions for reusable operations
- To work with JSON files
- To implement CRUD operations
- To handle invalid user input
- To implement exception handling
- To organize a Python project properly
- To understand basic Git and GitHub workflow

---

## Technologies Used

- Python 3
- JSON
- File Handling
- Object-Oriented Programming
- Exception Handling
- Git
- GitHub

---

##  Project Structure

```text
student-management-system/
│
├── main.py
├── student.py
├── student_data.json
└── README.md

## File Description

1. main.py

This is the main application file.

It is responsible for:

Displaying the application menu
Taking input from the user
Calling student management functions
Validating user input
Handling user errors
Controlling the application flow

The program starts from:

if __name__ == "__main__":
    main()
2. student.py

This file contains the main student-related logic.

It contains:

Student class
Student object creation
JSON reading
JSON writing
Add student functionality
Search student functionality
Update student functionality
Delete student functionality
Student ID generation

The Student class represents an individual student.

Example:

class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

3. student_data.json

This file is used to permanently store student records.

Initially, the file contains: []

After adding students, the file may look like:

[
    {
        "student_id": 1,
        "name": "Sriharini",
        "age": 22,
        "course": "Python",
        "email": "sriharini@gmail.com"
    },
    {
        "student_id": 2,
        "name": "Rahul",
        "age": 23,
        "course": "Java",
        "email": "rahul@gmail.com"
    }
]

The application automatically reads and updates this file.

------------------Features----------------------------------
1. Add Student

The user can add a new student by entering:

Name
Age
Course
Email

The system automatically generates the student ID.

Example:

--- ADD STUDENT ---

Enter name: Sriharini
Enter age: 22
Enter course: Python
Enter email: sriharini@gmail.com

Student added successfully!
Student ID: 1
2. View All Students

Displays all students stored in the JSON file.

Example:

--- ALL STUDENTS ---

-------------------------------------------------------------------------------------
ID   Name                Age     Course              Email
-------------------------------------------------------------------------------------
1    Sriharini           22      Python              sriharini@gmail.com
2    Rahul               23      Java                rahul@gmail.com
-------------------------------------------------------------------------------------
3. Search Student

The user can search for a student using the student ID.

Example:

--- SEARCH STUDENT ---

Enter student ID: 1

Student Details
------------------------------
ID     : 1
Name   : Sriharini
Age    : 22
Course : Python
Email  : sriharini@gmail.com

If the student does not exist:

Student not found.
4. Update Student

The user can update an existing student's:

Name
Age
Course
Email

Example:

--- UPDATE STUDENT ---

Enter student ID: 1

Enter new information.
Enter name: Sriharini Chennu
Enter age: 22
Enter course: Python Full Stack
Enter email: sriharini@gmail.com

Student updated successfully.
5. Delete Student

The user can delete a student using the student ID.

The application asks for confirmation before deleting.

Example:

--- DELETE STUDENT ---

Enter student ID: 1

Student Name: Sriharini

Are you sure you want to delete? (y/n): y

Student deleted successfully.