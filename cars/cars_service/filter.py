from dataclasses import dataclass, field
from cars.model import Car
from typing import Callable
from functools import cmp_to_key
from collections import defaultdict


@dataclass
class FilterService:
    cars: list[Car] = field(default_factory=list[Car])

    def filter_cars(self, filter_fn: Callable[[Car], bool]) -> list[Car]:
        return [car for car in self.cars if filter_fn(car)]

    def get_cars_with_higher_mileage_than(self, mileage_limit: int) -> list[Car]:
        return self.filter_cars(lambda car: car.has_mileage_higher_than(mileage_limit))

    def sort_by_model(self, car_1: Car, car_2: Car) -> int:
        return (car_1.model > car_2.model) - (car_1.model < car_2.model)

    def get_cars_with_price_between(self, min_pirce: int, max_price: int) -> list[Car]:
        matching_cars = self.filter_cars(lambda car: car.has_price_between(min_pirce, max_price))
        return sorted(matching_cars, key=lambda car: car.model)
        # return sorted(matching_cars, key=cmp_to_key(self.sort_by_model))

    def get_extreme_priced_cars(self, extreme_fn: Callable[[list[int]], int]) -> Car | list[Car]:
        grouped_by_price = defaultdict(list)
        for car in self.cars:
            grouped_by_price[car.price].append(car)

        extreme_value = extreme_fn(list(grouped_by_price.keys()))
        return grouped_by_price[extreme_value]
