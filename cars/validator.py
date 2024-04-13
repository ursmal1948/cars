from abc import ABC, abstractmethod
from typing import Any
import re


class Validator(ABC):
    @abstractmethod
    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        pass


class CarsValidator(Validator):

    def __init__(self, model_regex: str, colors: list[str]) -> None:
        self.validation_functions = {
            'model': self.validate_model,
            'price': self.validate_price,
            'color': self.validate_color,
            'mileage': self.validate_mileage,
            'components': self.validate_components
        }
        self.model_regex = model_regex
        self.colors = colors

    def validate_model(self, model: str) -> bool:
        if re.match(self.model_regex, model):
            return True
        return False

    @staticmethod
    def validate_price(price: int) -> bool:
        return price > 0

    def validate_color(self, color: str) -> bool:
        return color in self.colors

    @staticmethod
    def validate_mileage(mileage: int) -> bool:
        return mileage > 0

    def validate_components(self, components: list[str]) -> bool:
        return all(re.match(self.model_regex, c) for c in components)

    def validate_car(self, car_data: dict[str, Any]) -> dict[str, Any]:
        errors = {}
        for attr, func in self.validation_functions.items():
            if attr in car_data:
                if not func(car_data[attr]):
                    errors[attr] = [f'Validation failed for {attr}']
            else:
                errors[attr] = [f'{attr} not found']
        # print(errors)
        return errors

    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        validated_cars_data = []
        for car_data in data:
            errors = self.validate_car(car_data)
            if not errors:
                validated_cars_data.append(car_data)
        return validated_cars_data

# data2 = [{'model': 'AUDI', 'price': 900, 'color': 'SILVER', 'mileage': 1200, 'components': ['ABS', 'BLUETOOTH']},
#          {'model': 'BMW', 'price': 300, 'color': 'WHITE', 'mileage': 500,
#           'components': ['AIR CONDITIONING', 'CAMERA']}]
# cv = CarsValidator(model_regex=r'^[A-Z\s]+$', colors=['SILVER', 'GREEN', 'WHITE', 'BLUE'])
# print(cv.validate(data2))
