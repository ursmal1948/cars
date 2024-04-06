from cars.model import Car
from cars.file.service import JsonFileService


class CarsFileReader:
    # validator = Validator
    # file_service_factory = FileServiceFactory
    def get_cars(self, filename: str) -> list[Car]:
        cars_data = JsonFileService.get_lines(filename, 'cars')
        cars = []
        pass
