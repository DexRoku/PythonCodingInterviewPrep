## Think of class as a blue print and an object as real item built from that blueprint

class Car:
    ## __init__ means "initialize". 
    ## In intitalization we define the properties that we want to use like here brand color etc
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is my new car.")

my_car = Car("Landrover", "Black")
my_car.drive()

class Sandwich:

    def __init__(self,bread_type,filing):
        self.bread_type = bread_type
        self.filing = filing

    def describe(self):
        print(f"This is a {self.filing} sandwich with {self.bread_type} bread")

sandwich = Sandwich("Cheese", "Wholegrain")
sandwich.describe()