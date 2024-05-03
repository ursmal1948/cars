import pytest
from cars.model import Car
from cars.cars_service.group_and_sort import GroupAndSortService


@pytest.fixture
def group_and_sort_service_with_duplicate_color_cars(group_and_sort_service, audi_car):
    group_and_sort_service.add_cars(audi_car)
    return group_and_sort_service


class TestGroupAndSortServiceGroupByColor:

    def test_when_all_have_different_colours(self, group_and_sort_service):
        result = group_and_sort_service.group_by_color()
        assert result == {'WHITE': 1, 'BLUE': 1, 'SILVER': 1}

    def test_when_more_than_one_of_same_colour(self, group_and_sort_service_with_duplicate_color_cars):
        result = group_and_sort_service_with_duplicate_color_cars.group_by_color()
        assert result == {'WHITE': 1, 'BLUE': 2, 'SILVER': 1}

    def test_when_all_have_same_colour(self):
        service = GroupAndSortService([
            Car("A", 1, "SILVER", 20, []),
            Car("B", 2, "SILVER", 30, []),
            Car("C", 3, "SILVER", 40, [])
        ])
        assert service.group_by_color() == {'SILVER': 3}
