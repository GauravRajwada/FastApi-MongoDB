# FastApi-MongoDB 

This repository sample the implementation of an ecommerce application API, which includes endpoints for listing products and placing orders. Below is the directory structure and brief description of each file:

## Directory Structure

📦 ecommerce-api <br>
┣ 📂 domain <br>
┃ ┗ 📜 orders.py # Main file for connecting to the database and returning responses related to orders <br>
┣ 📂 message <br>
┃ ┗ 📜 orders.py # Pydantic validators for API messages <br>
┣ 📂 utils <br>
┃ ┗ 📜 database.py # Utility functions for database operations <br>
┃ ┗ 📜 constant.py # Constants used throughout the repository <br>
┣ 📜 App.py # Main FastAPI app <br>
┣ 📜 README.md # This file <br>
┗ 📜 requirements.txt # Dependencies <br>



## Files Description

### App.py
Main entry point of the FastAPI application. It includes routing setup and basic API endpoints.

### domain/orders.py
This file contains the main functions responsible for interacting with the database to retrieve products and place orders.

### message/orders.py
Defines Pydantic models for validating API request and response messages related to orders.

### utils/database.py
Contains utility functions for performing database operations, such as fetching records and inserting data.

### utils/constant.py
Defines constants used throughout the repository, such as table names and API response structures.


## Endpoint
### GET ```/api/get-products/```
![Products API Screenshot](https://github.com/GauravRajwada/FastApi-MongoDB/raw/master/Screenshot/products%20api.png)
## Endpoint
### GET ```/api/place-order/```
![Place Order API Screenshot](https://github.com/GauravRajwada/FastApi-MongoDB/raw/master/Screenshot/placeorderapi.png)


