from typing import Any
import re
from dataclasses import dataclass
from typing import Callable
from abc import ABC, abstractmethod


@dataclass
class Validator:
    validation_functions: dict[str, Callable[[Any], bool]]

    def validate_item(self, item_data: dict[str, Any]) -> dict[str, list[str]]:
        errors = {}
        for attr, func in self.validation_functions.items():
            if attr in item_data:
                if not func(item_data[attr]):
                    errors[attr] = [f'Validation failed for {attr}']
            else:
                errors[attr] = [f'{attr} not found']
        return errors

    # @abstractmethod
    # def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    #     pass


class CarsDataValidator(Validator):

    def __init__(self, model_regex: str, colors: list[str], price_min: int = 0) -> None:
        super().__init__({
            'model': self._validate_model,
            'price': self._validate_price,
            'color': self._validate_color,
            'mileage': self._validate_mileage,
            'components': self._validate_components
        })
        self.model_regex = model_regex
        self.colors = colors
        self.price_min = price_min

    def _validate_model(self, model: str) -> bool:
        if re.match(self.model_regex, model):
            return True
        return False

    def _validate_price(self, price: int) -> bool:
        return price > self.price_min

    def _validate_color(self, color: str) -> bool:
        return color in self.colors

    def _validate_mileage(self, mileage: int) -> bool:
        return mileage > self.price_min

    def _validate_components(self, components: list[str]) -> bool:
        return all(re.match(self.model_regex, c) for c in components)

    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [car for car in data if len(self.validate_item(car)) == 0]
