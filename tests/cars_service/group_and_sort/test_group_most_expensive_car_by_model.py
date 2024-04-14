from cars.cars_service.group_and_sort import GroupAndSortService
from cars.model import Car


class TestCarsService:
    CAR_1 = Car('A', 1, 'WHITE', 10, [])
    CAR_2 = Car('B', 2, 'BLUE', 20, [])
    CAR_3 = Car('C', 3, 'SILVER', 30, [])
    CAR_4 = Car('A', 1, 'BLACK', 30, [])


class TestGroupAndSortServiceGroupMostExpensiveCarsByModel:

    def test_when_models_have_one_most_expensive_car(self):
        cars_service = GroupAndSortService(
            [TestCarsService.CAR_1,
             TestCarsService.CAR_2,
             TestCarsService.CAR_3,
             ]
        )
        result = cars_service.group_most_expensive_cars_by_model()
        assert result == {'A': Car('A', 1, 'WHITE', 10, []),
                          'B': Car('B', 2, 'BLUE', 20, []),
                          'C': Car('C', 3, 'SILVER', 30, [])}

    def test_when_models_have_more_than_one_most_expensive_car(self):
        cars_service = GroupAndSortService(
            [TestCarsService.CAR_1,
             TestCarsService.CAR_2,
             TestCarsService.CAR_3,
             TestCarsService.CAR_4
             ]
        )
        result = cars_service.group_most_expensive_cars_by_model()
        assert result == {'A': [Car('A', 1, 'WHITE', 10, []),
                                Car('A', 1, 'BLACK', 30, [])],
                          'B': Car('B', 2, 'BLUE', 20, []),
                          'C': Car('C', 3, 'SILVER', 30, [])}
