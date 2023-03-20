from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self,distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_CONSTANT = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self,distance):
        self.fuel_quantity -= distance * (self.fuel_consumption + self.SUMMER_CONSTANT)


    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.FILL_CONSTANT = 0.95
        self.SUMMER_CONSTANT = 1.6

    def drive(self, distance):
        self.fuel_quantity -= distance * (self.fuel_consumption + self.SUMMER_CONSTANT)

    def refuel(self, fuel):
        self.fuel_quantity += fuel*self.FILL_CONSTANT

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)




