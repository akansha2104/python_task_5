
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display_info(self):
        return f"Vehicle name: {self.name}, Model: {self.model}"

# First derived class
class Car(Vehicle):
    def __init__(self, name, model, doors):
        super().__init__(name, model)  
        self.doors = doors

    def display_car_info(self):
        return f"{self.display_info()}, Doors: {self.doors}"

# Second derived class
class ElectricCar(Car):
    def __init__(self, name, model, doors, battery_capacity):
        super().__init__(name, model, doors)  
        self.battery_capacity = battery_capacity

    def display_electric_car_info(self):
        return f"{self.display_car_info()}, Battery Capacity: {self.battery_capacity} kWh"

electric_car = ElectricCar("Tesla", "Model S", 4, 100)

print(electric_car.display_electric_car_info())
