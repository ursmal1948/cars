# 🚘 Car Data Retrieval and Processing Project 🚘


<div align="center">
    <img src="car.svg" alt="Logo" style="width: 150px; height: auto;">
    <h1 style="color:lightyellow;"> 🏁 CARS 🏁 </h1>
  <div align="center">
    <img src="coverage.svg" alt="coverage"> 
</div>
</div>
<div>
<h2 id="about">

## About

This project simplifies retrieving car data from multiple sources. Using an abstract factory pattern, it gathers information
  from JSON and TXT files, offering a flexible and efficient solution for data extraction.



## Key Features
- Data Retrieval: Fetching data from various sources, including JSON and TXT files, enabling users to access car information from diverse datasets.
- Data Validation: Before conversion, validation of the retrieved data, ensuring integrity and accuracy.
- Data Conversion: Leveraging an abstract factory pattern, conversion of the retrieved data into Car instances.
## Cars Service
- The Filter service class provides a comprehensive filtering mechanism for car data. Users can easily extract subsets of cars that meet particular requirements,
such as mileage limits or price ranges. 
- The GroupAndSort service class offers comprehensive sorting functionalities for car data, allowing users to organize their datasets based on various criteria.
Users can easily sort their car collections by specific attributes such as price, mileage, or model.
- The Statistics service class calculates essential statistical information, such as the minimum, average, and maximum values, for a specified category of cars, such as price or mileage. Users can gain valuable insights into their car datasets.
## Design Patterns
Abstract Factory Pattern
The abstract factory pattern is used to create families of related or dependent objects without specifying their concrete classes. In this project, it facilitates the following tasks:

- Gathering Data: The abstract factory pattern retrieves car data from various sources, such as JSON and TXT files. This allows the system to handle multiple data formats seamlessly.
- Data Validation: Before converting the raw data into Car instances, the abstract factory ensures that the data is validated for integrity and accuracy, preventing errors in the subsequent stages.
- Data Conversion: Once validated, the abstract factory converts the retrieved data into Car instances. This encapsulates the creation logic and ensures that Car objects are consistently and correctly instantiated.
By leveraging the abstract factory pattern, the project achieves scalability and flexibility, making it easy to add new data sources in the future and maintain a clean separation of concerns.

Builder Pattern
The builder pattern is employed to construct complex objects step by step. In this project, it is used to create Car instances. This creational pattern allows for more controlled and simpler object creation, enabling
for customization of Car instances according to specific requirements or preferences. 

## Asynchronous Data Processing Approach on branch async-feature
DataProcessor is an asynchronous data processing utility designed to handle data conversion from TXT and JSON formats. Utilizing asynchronous processing, it offers efficient validation and conversion of car data, ensuring high-performance operations for diverse data sources.
## Test Coverage
The test coverage for this project has been assessed using both pytest and unittest frameworks. By implementing these testing frameworks, comprehensive tests have been developed to ensure the reliability and correctness of the functionalities. 



