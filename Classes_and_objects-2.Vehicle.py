class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):

    def __init__(self,name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def bus_info(self):
        return f'school bus {self.name} maxspeed:{self.max_speed} mileage: {self.mileage}'


school_bus = Bus('Volvo', 180, 12)
print(school_bus.bus_info())
