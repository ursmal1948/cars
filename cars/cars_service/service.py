from dataclasses import dataclass, field
from cars.model import Car


@dataclass
class CarsService:
    cars: list[Car] = field(default_factory=list[Car])

    def get_cars(self) -> list[Car]:
        return self.cars

    def add_cars(self, cars: Car | list[Car]) -> None:
        if isinstance(cars, Car):
            self.get_cars().append(cars)
        elif isinstance(cars, list) and all(isinstance(car, Car) for car in cars):
            self.get_cars().extend(cars)
