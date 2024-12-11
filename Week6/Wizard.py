class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        
class Student(Wizard):
    def __init__ (self, name ,house):
        super().__init__(name)
        self.house = house
    
class Professor(Wizard):
    def __init__ (self, name ,subject):
        super().__init__(name)
        self.subject = subject
        
wizard = Wizard("Albus")
student = Student("Luna Lovegood", "Ravenclaw")
professor = Professor("Gonnagal", "Transfigurasi")

print(wizard.name)
print(f"{student.name} is in {student.house}")
print(f"{professor.name} teaches {professor.subject}")