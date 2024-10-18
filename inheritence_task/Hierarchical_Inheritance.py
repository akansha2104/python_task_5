class College:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return f"College Name: {self.name}, Location: {self.location}"

class EngineeringCollege(College):
    def __init__(self, name, location, courses_offered):
        super().__init__(name, location)  # Call the constructor of the College class
        self.courses_offered = courses_offered

    def display_engineering_info(self):
        return f"{self.display_info()}, Courses Offered: {', '.join(self.courses_offered)}"

class ArtsCollege(College):
    def __init__(self, name, location, programs_offered):
        super().__init__(name, location)  # Call the constructor of the College class
        self.programs_offered = programs_offered

    def display_arts_info(self):
        return f"{self.display_info()}, Programs Offered: {', '.join(self.programs_offered)}"

engineering_college = EngineeringCollege("anjuman college of engineering and technology", "Nagpur", ["Computer Science", "Mechanical Engineering"])
arts_college = ArtsCollege("G.H Raisoni", "Pune", ["Fine Arts", "Literature"])

print(engineering_college.display_engineering_info())
print(arts_college.display_arts_info())
