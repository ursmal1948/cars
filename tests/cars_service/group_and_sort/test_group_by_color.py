from cars.model import Car
from cars.cars_service.group_and_sort import GroupAndSortService


class TestCarsService:
    CAR_1 = Car('A', 1, 'WHITE', 10, [])
    CAR_2 = Car('B', 2, 'BLUE', 20, [])
    CAR_3 = Car('C', 3, 'SILVER', 30, [])


class TestGroupAndSortServiceGroupByColor:

    def test_when_all_have_different_colours(self):
        service = GroupAndSortService([
            TestCarsService.CAR_1,
            TestCarsService.CAR_2,
            TestCarsService.CAR_3
        ])
        result = service.group_by_color()
        assert result == {'WHITE': 1, 'BLUE': 1, 'SILVER': 1}

    def test_when_more_than_one_of_same_colour(self):
        service = GroupAndSortService([
            TestCarsService.CAR_1,
            TestCarsService.CAR_2,
            TestCarsService.CAR_1,
        ])
        result = service.group_by_color()
        assert result == {'WHITE': 2, 'BLUE': 1}

    def test_when_all_have_same_colour(self):
        service = GroupAndSortService([
            TestCarsService.CAR_3,
            TestCarsService.CAR_3,
            TestCarsService.CAR_3
        ])
        assert service.group_by_color() == {'SILVER': 3}
