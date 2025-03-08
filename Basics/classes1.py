class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"


car1 = Car("Toyota", "Camry", 2016)
print(car1.display_info())
