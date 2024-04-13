from enum import Enum


class Color(Enum):
    SILVER = 1,
    GREEN = 2,
    WHITE = 3,
    BLUE = 4


class Category(Enum):
    PRICE = 0,
    MILEAGE = 1
    INVALID_CATEGORY = 2
