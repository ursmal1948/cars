from dataclasses import dataclass, field
from collections import defaultdict, Counter
from cars.model import Car
from typing import Callable
from functools import cmp_to_key


@dataclass
class GroupAndSortService:
    cars: list[Car] = field(default_factory=list[Car])

    def sort_cars(self, sort_fn: Callable[[Car, Car], bool]) -> list[Car]:
        return sorted(self.cars, key=cmp_to_key(sort_fn))

    @staticmethod
    def compare_cars(car1: Car, car2: Car, sorting_key: str) -> int:
        key_value1 = getattr(car1, sorting_key)
        key_value2 = getattr(car2, sorting_key)

        if key_value1 == key_value2:
            return 0
        elif key_value1 < key_value2:
            return -1
        else:
            return 1

    def sort_by(self, sorting_key: str) -> list[Car]:
        if not all(hasattr(car, sorting_key) for car in self.cars):
            raise AttributeError('Incorrect key')
        return self.sort_cars(sort_fn=lambda car1, car2: self.compare_cars(car1, car2, sorting_key))

    def group_by_color(self) -> dict[str, int]:
        cnt = Counter()
        for car in self.cars:
            cnt[car.color] += 1
        return dict(sorted(cnt.items(), key=lambda e: e[1], reverse=True))

    def get_most_expensive_car_for_model(self, model: str) -> Car | list[Car]:
        grouped_by_price = defaultdict(list)
        for car in self.cars:
            if car.model == model:
                grouped_by_price[car.price].append(car)
        most_expensive = max(grouped_by_price.keys())
        result = grouped_by_price[most_expensive]
        return result if len(result) > 1 else result[0]

    def group_most_expensive_car_by_model(self) -> dict[str, list[Car]]:
        most_expensive_car_by_model = defaultdict(list)
        unique_models = set(car.model for car in self.cars)
        for model in unique_models:
            most_expensive_car_by_model[model] = self.get_most_expensive_car_for_model(model)
        return dict(sorted(most_expensive_car_by_model.items(), key=lambda e: [0]))

    def group_cars_by_component(self) -> dict[str, list[Car]]:
        unique_components = set(car.component for car in self.cars for car.component in car.components)
        return {component: [car for car in self.cars if car.has_component(component)] for component in
                unique_components}
