import pytest
from cars.file.reader import JsonFileService


class TestJsonFileServiceGetLinesPathNotCorrect:
    def test_when_path_has_incorrect_extension(self):
        with pytest.raises(AttributeError) as e:
            JsonFileService().get_lines('test_data/cars_test.png', 'key')
        assert str(e.value) == 'File has incorrect extension'

    def test_when_path_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            JsonFileService().get_lines('test_data/cars_testt.json', 'key')
        assert str(e.value).startswith('File not found')

    def test_when_key_not_found(self):
        with pytest.raises(AttributeError) as e:
            JsonFileService().get_lines('test_data/cars_test.json', 'people')
        assert str(e.value).startswith('Key not found')


class TestJsonFileServiceGetLinesEmptyContent:
    def test_when_file_has_no_content(self):
        data = JsonFileService().get_lines('test_data/empty_cars_test.json', 'cars')
        assert len(data) == 0


class TestJsonFileServiceGetLinesContentCorrect:
    def test_when_content_present(self):
        data = JsonFileService().get_lines('test_data/cars_test.json', 'cars')
        assert len(data) == 3
        assert list(data[0].values()) == ['AUDI', 9000, 'SILVER', 1500, ['CAMERA']]
        assert list(data[1].values()) == ['BMW', 3000, 'WHITE', 2800, ['KEYLESS ENTRY']]
        assert list(data[2].values()) == ['TOYOTA', 4000, 'BLUE', 10000, ['KEYLESS ENTRY', 'BLUETOOTH']]
