class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id

    def display_student_info(self):
        return f"{self.display_info()}, Student ID: {self.student_id}"

students = [
    Student("Akansha", 20, "S54321"),
    Student("ashu", 22, "S67890"),
    Student("ankita", 24, "S14253")
]

for student in students:
    print(student.display_student_info())
