import logging

import pytest
from cars.file.reader import JsonFileService
from cars.file.reader import TxtFileService
import asyncio


class TestJsonFileServiceGetLines:
    @pytest.mark.asyncio
    async def test_when_path_has_incorrect_extension(self):
        with pytest.raises(FileNotFoundError) as e:
            await JsonFileService().get_lines('test_data/cars_test.png', 'key')
        assert e.errisinstance(FileNotFoundError)

    @pytest.mark.asyncio
    async def test_when_path_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            await JsonFileService().get_lines('test_data/cars_testt.json', 'key')
        assert e.errisinstance(FileNotFoundError)

    @pytest.mark.asyncio
    async def test_when_key_not_found(self, json_path_correct_data):
        with pytest.raises(KeyError) as e:
            await JsonFileService().get_lines(json_path_correct_data, 'people')
        assert e.errisinstance(KeyError)

    @pytest.mark.asyncio
    async def test_when_file_has_no_content(self):
        data = await JsonFileService().get_lines('test_data/empty_cars_test.json', 'cars')
        assert len(data) == 0

    @pytest.mark.asyncio
    async def test_when_content_present(self, json_path_correct_data):
        data = await JsonFileService().get_lines(json_path_correct_data, 'cars')
        assert len(data) == 3
        assert list(data[0].values()) == ['AUDI', 9000, 'SILVER', 1500, ['CAMERA']]
        assert list(data[1].values()) == ['BMW', 3000, 'WHITE', 2800, ['KEYLESS ENTRY']]
        assert list(data[2].values()) == ['TOYOTA', 4000, 'BLUE', 10000, ['KEYLESS ENTRY', 'BLUETOOTH']]


class TestTxtFileServiceGetLinesPathNotCorrect:

    @pytest.mark.asyncio
    async def test_when_path_has_incorrect_extension(self):
        with pytest.raises(FileNotFoundError) as e:
            await TxtFileService().get_lines('test_data/cars_test.jpg')
        assert e.errisinstance(FileNotFoundError)

    @pytest.mark.asyncio
    async def test_when_path_not_found(self):
        with pytest.raises(FileNotFoundError) as e:
            await TxtFileService().get_lines('test_data/cars_testt.txt')
        assert e.errisinstance(FileNotFoundError)

    @pytest.mark.asyncio
    async def test_when_file_has_no_content(self):
        content = await TxtFileService().get_lines('test_data/empty_cars_test.txt')
        assert content == []

    @pytest.mark.asyncio
    async def test_when_file_has_wrong_content(self):
        with pytest.raises(ValueError) as e:
            await TxtFileService().get_lines('test_data/wrong_content_cars_test.txt')
        assert e.errisinstance(ValueError)

    @pytest.mark.asyncio
    async def test_when_content_present(self, txt_path_correct_data):
        content = await TxtFileService().get_lines(txt_path_correct_data)
        assert len(content) == 2
        assert list(content[0].values()) == ['BMW', 2000, 'BLUE', 1500, ['BLUETOOTH', 'ABS']]
        assert list(content[1].values()) == ['OPEL', 1000, 'SILVER', 2000, ['CAMERA', 'ABS']]
