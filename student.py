class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("ID     :", self.student_id)
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Course :", self.course)
        print("Marks  :", self.marks)
        