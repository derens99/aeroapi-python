![Pytest](https://github.com/derens99/aeroapi-python/workflows/Run%20pytest/badge.svg)

# AeroApi Python

Python wrapper for the FlightAware's AeroAPI

## Description

AeroAPI (formerly FlightXML) is FlightAware's live flight data API that provides powerful, reliable information about real-time and historical flight information. This Python wrapper allows for easier interaction with the AeroAPI from Python applications.

## FlightAware AeroAPI Reference
[AeroAPI](https://flightaware.com/aeroapi)

## Installation

```bash
pip install aeroapi-python
```
    
### Using test pypi, install with this command.
```bash
pip install --index-url https://pypi.org/simple/ --extra-index-url https://test.pypi.org/simple/ aeroapi-python
```

## Usage

### AeroAPI Class
The AeroAPI class is the main class for interacting with the FlightAware AeroAPI. It provides access to various resources such as airports, operators, flights, and more.

#### Initialization
To use the AeroAPI class, you need to create an instance of it by passing your API key as an argument to the constructor:

```python
from AeroAPI import AeroAPI

api_key = 'your-api-key'
aeroapi = AeroAPI(api_key)
```

### Airports
The Airports class provides methods for retrieving information about airports. You can access an instance of the Airports class through the airports attribute of the AeroAPI instance:

```python
airports = aeroapi.airports
```

#### Methods

- get_airport_info(airport_code: str) -> dict: Returns information about the specified airport.
    
    ```python
    airport_info = airports.get_airport_info('KLAX')
    ```

- search_airports(query: str) -> list: Searches for airports that match the specified query.
    
    ```python
    airport_list = airports.search_airports('Los Angeles')
    ```

- get_nearby_airports(latitude: float, longitude: float, radius: int) -> list: Returns a list of airports near the specified latitude and longitude within the specified radius.
    
    ```python
    airport_list = airports.get_nearby_airports(33.9425, -118.408056, 10)
    ```

#### Example Usage

```python 
from AeroAPI import AeroAPI

api_key = 'your-api-key'
aeroapi = AeroAPI(api_key)

airports = aeroapi.airports
airport_info = airports.get_airport_info('KLAX')

print(airport_info)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@derens99](https://www.github.com/derens99)