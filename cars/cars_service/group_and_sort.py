from dataclasses import dataclass, field
from collections import defaultdict, Counter
from cars.model import Car
from typing import Callable
from functools import cmp_to_key


@dataclass
class GroupAndSortService:
    cars: list[Car] = field(default_factory=list[Car])

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
