class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name!!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #getter
    @property
    def house(self):
        return self._house
    
    #setter
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
        

def main():
    student = get_student_dict()
    print(student)
    
def get_student_dict():
    name = input("Nama :")
    house = input("House :")
    student = Student(name,house)
    return student

if __name__ == "__main__":
    main()