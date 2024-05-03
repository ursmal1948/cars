class TestGroupAndSortServiceGroupByComponent:

    def test_when_component_is_in_one_car(self, group_and_sort_service, toyota_car):
        result = group_and_sort_service.group_cars_by_component()['BLUETOOTH'][0]
        assert result == toyota_car

    def test_when_multiple_cars_have_same_component(self, group_and_sort_service, audi_car, bmw_car):
        result = group_and_sort_service.group_cars_by_component()['ABS']
        assert result == [
            bmw_car,
            audi_car
        ]
