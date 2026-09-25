import json
import os


class FileHandler:

    def __init__(self, filename):
        self.filename = filename

    def save(self, students):
        folder = os.path.dirname(self.filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        data = []

        for student in students:
            data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "marks": student.marks
            })

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []