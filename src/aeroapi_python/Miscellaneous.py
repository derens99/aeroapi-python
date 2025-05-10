from typing import Optional, Dict, Any
from aeroapi_python.APICaller import APICaller


class Miscellaneous:
    """
    A class for interacting with miscellaneous FlightAware AeroAPI.

    Attributes:
        api_caller (APICaller): An instance of the `APICaller` class.
        endpoint (str): The API endpoint for miscellaneous APIs.

    Methods:
        __init__(self, api_caller: APICaller) -> None:
            Initializes a `Miscellaneous` instance.

        aircraft_owner(self, ident: str) -> Optional[Dict[str, Any]]:
            Retrieves the owner of a specific aircraft.

        aircraft_type(self, aircraft_type: str) -> Optional[Dict[str, Any]]:
            Retrieves information about a specific aircraft type.

        global_disruption_counts(self, entity_type: str, time_period: str = 'today', max_pages: int = 1,
                                 cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves global disruption counts for a specific entity type.

        disruption_counts(self, entity_type: str, entity_id: str, time_period: str = 'today') -> Optional[Dict[str, Any]]:
            Retrieves disruption counts for a specific entity.

        scheduled_flights(self, date_start: str, date_end: str, origin: Optional[str] = None,
                           destination: Optional[str] = None, airline: Optional[str] = None,
                           flight_number: Optional[str] = None, include_codeshares: bool = True,
                           include_regional: bool = True, max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves scheduled flights for a specific time period and set of filters.
    """

    def __init__(self, api_caller: APICaller) -> None:
        """
        Initializes a `Miscellaneous` instance.

        Args:
            api_caller (APICaller): An instance of the `APICaller` class.
        """
        self.api_caller = api_caller
        self.endpoint = ""

    def aircraft_owner(self, ident: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the owner of a specific aircraft.

        Args:
            ident (str): The identifier of the aircraft.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        path = self.api_caller._build_path("aircraft", sub_path=f"{ident}/owner")
        return self.api_caller.get(path)

    def aircraft_type(self, aircraft_type: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about a specific aircraft type.

        Args:
            aircraft_type (str): The name of the aircraft type.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        path = self.api_caller._build_path(
            "aircraft", sub_path=f"types/{aircraft_type}"
        )
        return self.api_caller.get(path)

    def global_disruption_counts(
        self,
        entity_type: str,
        time_period: str = "today",
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves global disruption counts for a specific entity type.

        Args:
            entity_type (str): The type of entity to retrieve disruption counts for.
            time_period (str): Optional, the time period to retrieve disruption counts for (default 'today').
            max_pages (int): Optional, the maximum number of pages to retrieve (default 1).
            cursor (str): Optional, a cursor for pagination (default None).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {"time_period": time_period, "max_pages": max_pages, "cursor": cursor}
        path = self.api_caller._build_path(
            "disruption_counts", sub_path=f"{entity_type}", query=query
        )
        return self.api_caller.get(path)

    def disruption_counts(
        self, entity_type: str, entity_id: str, time_period: str = "today"
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves disruption counts for a specific entity.

        Args:
            entity_type (str): The type of entity to retrieve disruption counts for.
            entity_id (str): The identifier of the entity to retrieve disruption counts for.
            time_period (str): Optional, the time period to retrieve disruption counts for (default 'today').

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {"time_period": time_period}
        path = self.api_caller._build_path(
            "disruption_counts", sub_path=f"{entity_type}/{entity_id}", query=query
        )
        return self.api_caller.get(path)

    def scheduled_flights(
        self,
        date_start: str,
        date_end: str,
        origin: Optional[str] = None,
        destination: Optional[str] = None,
        airline: Optional[str] = None,
        flight_number: Optional[str] = None,
        include_codeshares: bool = True,
        include_regional: bool = True,
        max_pages: int = 1,
        cursor: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves scheduled flights for a specific time period and set of filters.

        Args:
            date_start (str): The start date of the search in YYYY-MM-DD format.
            date_end (str): The end date of the search in YYYY-MM-DD format.
            origin (str): Optional, the origin airport code.
            destination (str): Optional, the destination airport code.
            airline (str): Optional, the airline code.
            flight_number (str): Optional, the flight number.
            include_codeshares (bool): Optional, whether to include codeshare flights (default True).
            include_regional (bool): Optional, whether to include regional flights (default True).
            max_pages (int): Optional, the maximum number of pages to retrieve (default 1).
            cursor (str): Optional, a cursor for pagination (default None).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {
            "origin": origin,
            "destination": destination,
            "airline": airline,
            "flight_number": flight_number,
            "include_codeshares": include_codeshares,
            "include_regional": include_regional,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(
            "schedules", sub_path=f"{date_start}/{date_end}", query=query
        )
        return self.api_caller.get(path)
