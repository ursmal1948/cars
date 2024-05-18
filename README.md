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

## Asynchronos Data Processing Approach on branch async-feature
DataProcessor is an asynchronous data processing utility designed to handle data conversion from TXT and JSON formats. Utilizing asynchronous processing, it offers efficient validation and conversion of car data, ensuring high-performance operations for diverse data sources.
## Test Coverage
The test coverage for this project has been assessed using both pytest and unittest frameworks. By implementing these testing frameworks, comprehensive tests have been developed to ensure the reliability and correctness of the functionalities. 



