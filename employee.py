class Employee:
    def __init__(self, name, employee_ID, salary):
        self.name = name
        self.employee_ID = employee_ID
        self.salary = salary
        # method

    def display_info(self):
        print(f"name:{self.name}\nEmployee_ID:{self.employee_ID}\nsalary:${self.salary}")

    def calculate_salary(self):
        print(f"{self.salary * 12}")


class Manager(Employee):
    def __init__(self, name, employee_ID, salary, Department,employees_managed='none'):
        super().__init__(name, employee_ID, salary)
        self.Department = Department
        self.employees_managed = employees_managed if employees_managed else[]

    def add_employee(self, employee):
        self.employees_managed.append(employee)
    def display_employees_managed(self):
        print("Employees managed:")
        for employee in self.employees_managed:
            print(f"-{self.name} (ID:{self.employee_ID}")


    def display_info(self):
        super().display_info()
        print(f"Department:{self.Department}\nEmployees Managed:{[employee.name for employee in self.employees_managed]}")

    def calculate_salary(self):
        print(f" Annual salary is {self.salary * 12}")



class Developers(Employee):
    def __init__(self, name, employee_ID, salary,programming_language='none'):
        super().__init__(name, employee_ID, salary)
        self.programming_language=programming_language if programming_language else []
    def add_language(self,language):
        if language not in self.programming_language:
            self.programming_language.append(language)

    def display_info(self):
        super().display_info()
        print(f"Programming languages:{''.join(self.programming_languages)}")

    def calculate_salary(self):
        print(f"Annual salary is {self.salary * 12}")


class Interns(Employee):
    def __init__(self, name, employee_ID, salary, school_name, Graduation_year):
        super().__init__(name, employee_ID, salary)
        self.school_name = school_name
        self.Graduation_year = Graduation_year
        # method

    def display_info(self):
        print(
            f"name:{self.name}\nEmployee-ID:{self.employee_ID}\n salary:{self.salary}\n school_name:{self.school_name}\n graduation year:{self.Graduation_year}")

    def calculate_salary(self):
        print(f"salary is {self.salary * 12}")

        # object
# create employees
employee=Employee('Venessa',1000,20000)
manager=Manager('Ken',1011,500000,'ICT',["Developers",'interns'])
developer=Developers('Damaris', 2013,250000,['python','javascript'])
intern=Interns('Cynthia',2022,10000,'University of Nairobi',2023)


#display information
employee.display_info()
manager.display_info()
developer.display_info()
intern.display_info()

#Add
manager.add_employee('Developers')
developer.add_language('java')

#calculate salary
employee.calculate_salary()
manager.calculate_salary()
developer.calculate_salary()
intern.calculate_salary()




