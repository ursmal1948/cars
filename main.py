from cars.file.service import DataProcessor, DataFactoryType, FromJsonFileToCar, FromTxtFileToCar
import asyncio


async def main():
    data_processor = await DataProcessor.create_processor(DataFactoryType.FROM_TXT)
    result = await data_processor.process('test_data/cars_test.txt')
    print(result)
    data_processor2 = await  DataProcessor.create_processor(DataFactoryType.FROM_JSON)
    result2 = await  data_processor2.process('test_data/cars_test.json', 'cars')
    print(result2)


if __name__ == "__main__":
    asyncio.run(main())
