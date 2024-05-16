from cars.file.service import DataProcessor, DataFactoryType
import asyncio


async def main():
    data_processor = await DataProcessor.create_processor(DataFactoryType.FROM_TXT)
    data_processor2 = await DataProcessor.create_processor(DataFactoryType.FROM_JSON)
    result = await asyncio.gather(
        data_processor2.process('test_data/cars_test.json', 'cars'),
        data_processor.process('test_data/cars_test.txt'),
    )
    for cars in result:
        print(cars)


if __name__ == "__main__":
    asyncio.run(main())
