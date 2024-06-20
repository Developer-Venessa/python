class Cars:
    def __init__(self,model,yearofmanufacture,type,color):
        self.model=model
        self.yearofmanufacture=yearofmanufacture
        self.type=type
        self.color=color
        # method
    def display(self):
        print(f"My dream car is {self.model} manufactured in {self.yearofmanufacture} being a {self.type} in color {self.color}")
# object
my_type=Cars('MERCEDEES BENZ',2023,'E320','BLACK')
my_type.display()
my_type=Cars('TOYOTA',2019,'HARRIER','RED')
my_type.display()
my_type=Cars('MAZDA',2024,'CX5','WHITE')
my_type.display()
my_type=Cars('MAZDA',2010,'ATENZA','GREY')
my_type.display()