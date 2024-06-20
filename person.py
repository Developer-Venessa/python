class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def print_name(self):
        print(f"my name is {self.first_name},{self.last_name} and i'm {self.age} years old")

class Student(Person):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
myStudent=Student("venessa",'Anyango',23)
myStudent.print_name()
myStudent=Student("Damaris",'Anyango',27)
myStudent.print_name()

