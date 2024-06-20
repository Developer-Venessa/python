class Student:
    # constructor
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

        # method
    def display(self):
        print(self.first_name,self.last_name)

        # object
my_student=Student('Venessa','Anyango')
my_student.display()
my_student=Student('Dee','Etaba')
my_student.display()
my_student=Student('kim','ken')
my_student.display()
my_student=Student('maggie','Eric')
my_student.display()