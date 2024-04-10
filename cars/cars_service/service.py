from dataclasses import dataclass, field
from cars.model import Car


@dataclass
class CarsService:
    cars: list[Car] = field(default_factory=list[Car])

    def __str__(self):
        return [
            f'Car:{car.model} Price:{car.price} Color:{car.color} Milaege:{car.mileage} Components:{[c for c in car.components]}'
            for car in self.cars]
