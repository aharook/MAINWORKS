import abc

class Vehicle(abc.ABC):
    def __init__(self, fuel, distance):
        self.fuel = fuel
        self.__distance = distance

    @property
    def get_distance(self):
        return self.__distance
    
    @get_distance.setter
    def set_distance(self, distance):
        self.__distance = distance

    @abc.abstractmethod
    def fuel_consumption_calc(self):  # абстрактний
        pass

    # Віртуальний метод
    def info(self):
        return f"Транспорт з загальним запасом палива {self.fuel} Л"

    def __del__(self):
        print(f'Destructor called, {self.__class__.__name__} deleted.')

    def __str__(self):
        return f"Витрати транспорту на {self.get_distance} km: {self.fuel_consumption_calc()} liters"


class Bus(Vehicle):
    def __init__(self, fuel, distance): 
        super().__init__(fuel, distance)

    def fuel_consumption_calc(self):  # override (абстрактного)
        return self.fuel * self.get_distance / 100

    # Override (віртуального) 
    def info(self):
        return "Автобус для пасажирів"


class Truck(Vehicle):
    def __init__(self, fuel, distance):
        super().__init__(fuel, distance)

    def fuel_consumption_calc(self):  # override (абстрактного)
        return self.fuel * self.get_distance / 100




