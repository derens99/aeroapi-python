from typing import Any, Dict, Optional

from aeroapi_python.APICaller import APICaller


class Airports:
    """
    An Airport class for interacting with the FlightAware AeroAPI.
    """

    def __init__(self, api_caller: APICaller) -> None:
        """
        Initializes an `Airports` instance.

        Args:
            api_caller (Any): An instance of the `APICaller` class.
        """
        self.api_caller = api_caller
        self.endpoint = "airports"

    def get_airports(
        self, max_pages: int = 1, cursor: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves a list of all airports.
        Args:
            max_pages (int): Optional, the maximum number of pages to retrieve (default 1).
            cursor (str): Optional, a cursor for pagination (default None).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {"max_pages": max_pages, "cursor": cursor}
        path = self.api_caller._build_path(self.endpoint, query=query)
        return self.api_caller.get(path)

    def get_airport(self, airport_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        path = self.api_caller._build_path(self.endpoint, airport_id)
        return self.api_caller.get(path)

    def get_canonical(
        self, airport_id: str, code: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves the canonical information for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            code (str): Optional, the type of identifier to use in the response.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {"id_type": code}
        path = self.api_caller._build_path(
            self.endpoint, airport_id + "/canonical", query
        )
        return self.api_caller.get(path)

    def get_airports_with_delays(
        self, max_pages: int = 1, cursor: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves a list of airports with delays.

        Args:
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = "delays"
        query = {"max_pages": max_pages, "cursor": cursor}
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)

    def all_flights(
        self,
        airport_id: str,
        airline: Optional[str] = None,
        flight_type: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about all flights for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            airline (str): Optional, the airline to filter by.
            flight_type (str): Optional, the type of flight to filter by.
            start (int): Optional, the start timestamp for the flight data (Unix time).
            end (int): Optional, the end timestamp for the flight data (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/flights"
        query = {
            "airline": airline,
            "type": flight_type,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)

    def get_counts(self, airport_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the flight counts for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, airport_id + "/flights/counts")
        )

    def recent_arrivals(
        self,
        airport_id: str,
        airline: Optional[str] = None,
        flight_type: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about recent arrivals for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            airline (str): Optional, the airline to filter by.
            flight_type (str): Optional, the type of flight to filter by.
            start (int): Optional, the start timestamp for the flight data (Unix time).
            end (int): Optional, the end timestamp for the flight data (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/flights/arrivals"

        query = {
            "airline": airline,
            "type": flight_type,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }

        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        response = self.api_caller.get(path)  # Make API call

        return response  # Return parsed JSON response or None if the request failed

    def recent_departures(
        self,
        airport_id: str,
        airline: Optional[str] = None,
        flight_type: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about recent departures for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            airline (str): Optional, the airline to filter by.
            flight_type (str): Optional, the type of flight to filter by.
            start (int): Optional, the start timestamp for the flight data (Unix time).
            end (int): Optional, the end timestamp for the flight data (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/flights/departures"

        query = {
            "airline": airline,
            "type": flight_type,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }

        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        response = self.api_caller.get(path)  # Make API call

        return response  # Return parsed JSON response or None if the request failed

    def scheduled_arrivals(
        self,
        airport_id: str,
        airline: Optional[str] = None,
        flight_type: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about scheduled arrivals for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            airline (str): Optional, the airline to filter by.
            flight_type (str): Optional, the type of flight to filter by.
            start (int): Optional, the start timestamp for the flight data (Unix time).
            end (int): Optional, the end timestamp for the flight data (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/flights/scheduled_arrivals"

        query = {
            "airline": airline,
            "type": flight_type,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }

        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        response = self.api_caller.get(path)  # Make API call

        return response  # Return parsed JSON response or None if the request failed

    def scheduled_departures(
        self,
        airport_id: str,
        airline: Optional[str] = None,
        flight_type: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about scheduled departures for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            airline (str): Optional, the airline to filter by.
            flight_type (str): Optional, the type of flight to filter by.
            start (int): Optional, the start timestamp for the flight data (Unix time).
            end (int): Optional, the end timestamp for the flight data (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/flights/scheduled_departures"
        query = {
            "airline": airline,
            "type": flight_type,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)

    def get_nearby_airports(
        self,
        airport_id: str,
        radius: int,
        only_iap: bool = False,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about nearby airports for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            radius (int): The radius (in kilometers) to search for nearby airports.
            only_iap (bool): Optional, whether to only include airports with instrument
            approach procedures.
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/nearby"
        query = {
            "radius": radius,
            "only_iap": only_iap,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)

    def get_flights_between_airports(
        self,
        origin_id: str,
        dest_id: str,
        flight_type: Optional[str] = None,
        connection: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about flights between two airports.

        Args:
            origin_id (str): The origin airport identifier (ICAO code).
            dest_id (str): The destination airport identifier (ICAO code).
            flight_type (str): Optional, the type of flight to filter by.
            connection (str): Optional, the connection type to filter by.
            start (int): Optional, the start timestamp for the flight data (Unix time).
            end (int): Optional, the end timestamp for the flight data (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{origin_id}/flights/to/{dest_id}"
        query = {
            "type": flight_type,
            "connection": connection,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)

    def get_airport_weather_forecast(
        self,
        airport_id: str,
        timestamp: Optional[int] = None,
        return_nearby_weather: bool = False,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves the weather forecast for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            timestamp (int): Optional, the timestamp for the
            weather forecast (Unix time).
            return_nearby_weather (bool): Optional, whether to include nearby weather
            observations in the response.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/weather/forecast"
        query = {
            "timestamp": timestamp,
            "return_nearby_weather": return_nearby_weather,
        }
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)

    def get_airport_weather_conditions(
        self,
        airport_id: str,
        temperature_units: str = "Celsius",
        return_nearby_weather: bool = False,
        timestamp: Optional[int] = None,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves the weather conditions for a specific airport.

        Args:
            airport_id (str): The airport identifier (ICAO code).
            temperature_units (str): Optional, the temperature units to use in the
            response ('Celsius' or 'Fahrenheit').
            return_nearby_weather (bool): Optional, whether to include nearby weather
            observations in the response.
            timestamp (int): Optional, the timestamp for the
            weather conditions (in Unix time).
            max_pages (int): Optional, the maximum number of pages to retrieve.
            cursor (str): Optional, a cursor for paginating through the results.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{airport_id}/weather/observations"
        query = {
            "temperature_units": temperature_units,
            "return_nearby_weather": return_nearby_weather,
            "timestamp": timestamp,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(
            self.endpoint, sub_path=sub_path, query=query
        )
        return self.api_caller.get(path)
