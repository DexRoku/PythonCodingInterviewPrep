class Laptop:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        print(f"{self.brand} is now on.")

l = Laptop("Lenovo")
l.turn_on()
