from cars.cars_service.filter import FilterService
from cars.model import Car


class CarServiceData:
    CAR_1 = Car('BMW', 100, 'WHITE', 2000, [])
    CAR_2 = Car('AUDI', 100, 'BLUE', 1000, [])
    CAR_3 = Car('TOYOTA', 500, 'SILVER', 200, [])
    CAR_4 = Car('OPEL', 500, 'BLACK', 300, [])


class TestFilterServiceGetExtremePricedCars:
    def test_when_there_is_more_than_one(self):
        filter_service = FilterService([
            CarServiceData.CAR_1,
            CarServiceData.CAR_2,
            CarServiceData.CAR_3,
            CarServiceData.CAR_4
        ])
        most_priced_cars = filter_service.get_extreme_priced_cars(lambda cars: max(cars))
        assert most_priced_cars == [Car('TOYOTA', 500, 'SILVER', 200, []),
                                    Car('OPEL', 500, 'BLACK', 300, [])]

        least_prices_cars = filter_service.get_extreme_priced_cars(lambda cars: min(cars))
        assert least_prices_cars == [Car('BMW', 100, 'WHITE', 2000, []),
                                     Car('AUDI', 100, 'BLUE', 1000, [])]

    def test_when_there_is_one(self):
        filter_service = FilterService([CarServiceData.CAR_1, CarServiceData.CAR_3])
        assert filter_service.get_extreme_priced_cars(lambda cars: max(cars)) == Car('TOYOTA', 500, 'SILVER', 200, [])
        assert filter_service.get_extreme_priced_cars(lambda cars: min(cars)) == Car('BMW', 100, 'WHITE', 2000, [])
