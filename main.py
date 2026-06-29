class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Age": self.age,
            "Grade": self.grade
        }
