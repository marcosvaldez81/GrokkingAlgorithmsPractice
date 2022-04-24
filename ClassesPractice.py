###################

# Classes practice with Inheritance

###################


# Parent class
class Person:
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name 
        
        
    def print_name(self):
        print(self.first_name, self.last_name)
        
        

class Student(Person):
    def __init__(self,first_name,last_name,year):
        super().__init__(first_name, last_name)
        self.graduationyear = year
        
    

my_student = Student("Marcos", "Valdez", 2022)

print(my_student.print_name())
