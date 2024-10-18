class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name

    def display_department(self):
        return f"Department: {self.dept_name}"

class Position:
    def __init__(self, job_title):
        self.job_title = job_title

    def display_position(self):
        return f"Position: {self.job_title}"

class Employee(Department, Position):
    def __init__(self, name, age, dept_name, job_title):
        Department.__init__(self, dept_name)  
        Position.__init__(self, job_title)
        self.name = name
        self.age = age

    def display_employee_info(self):
        return f"Name: {self.name}, Age: {self.age}, {self.display_department()}, {self.display_position()}"

employees = [
    Employee("Ram", 30, "IT", "Software Engineer"),
    Employee("Shyam", 28, "HR", "Recruiter"),
    Employee("Sita", 35, "Finance", "Accountant"),
    Employee("gita", 40, "IT", "System Administrator")
]

for employee in employees:
    print(employee.display_employee_info())
