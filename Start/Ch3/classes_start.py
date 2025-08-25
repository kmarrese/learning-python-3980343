# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
    def __init__(self, mk, mdl, yr):
        self.make = mk
        self.model = mdl
        self.year = yr


    def display_info(self):
        print(f"Vehicle Information: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, mk, mdl, yr, eng):
        super().__init__(mk, mdl, yr)
        self.engine = eng

    def display_info(self):
        super().display_info()
        print(f"Engine type: {self.engine}")

car1 = Car("Honda", "Accord", 2020, "2.0l Turbo")
mc1 = Vehicle("Harley-Davidson", "Fat Boy", 2021)

car1.display_info()
mc1.display_info()
