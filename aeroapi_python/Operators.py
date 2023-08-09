from typing import Optional, Dict, Any
from aeroapi_python.APICaller import APICaller


class Operators:
    """
    A class for interacting with the FlightAware AeroAPI Operators API.

    Attributes:
        api_caller (APICaller): An instance of the `APICaller` class.
        endpoint (str): The API endpoint for the Operators API.

    Methods:
        __init__(self, api_caller: APICaller) -> None:
            Initializes an `Operators` instance.

        get_all_operators(self, max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves a list of operator references.

        get_operator_info(self, operator_id: str) -> Optional[Dict[str, Any]]:
            Retrieves static information for a specific operator.

        get_canonical_code(self, operator_id: str, country_code: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves the canonical code for a specific operator.

        get_operator_flights(self, operator_id: str, start: Optional[str] = None, end: Optional[str] = None,
                              max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves recent and upcoming flights for a specific operator.
    """

    def __init__(self, api_caller: APICaller) -> None:
        """
        Initializes an `Operators` instance.

        Args:
            api_caller (APICaller): An instance of the `APICaller` class.
        """
        self.api_caller = api_caller
        self.endpoint = 'operators'

    def get_all_operators(self, max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves a list of operator references.

        Args:
            max_pages (int): Optional, the maximum number of pages to retrieve (default 1).
            cursor (str): Optional, a cursor for pagination (default None).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {
            "max_pages": max_pages,
            "cursor": cursor
        }
        path = self.api_caller._build_path(self.endpoint, query=query)
        return self.api_caller.get(path)

    def get_operator_info(self, operator_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves static information for a specific operator.

        Args:
            operator_id (str): The ICAO or IATA identifier for the operator.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        path = self.api_caller._build_path(self.endpoint, sub_path=operator_id)
        return self.api_caller.get(path)

    def get_canonical_code(self, operator_id: str, country_code: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves the canonical code for a specific operator.

        Args:
            operator_id (str): The ICAO or IATA identifier for the operator.
            country_code (str): Optional, an ISO 3166-1 alpha-2 country code.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        sub_path = f"{operator_id}/canonical"
        query = {
            "country_code": country_code
        }
        path = self.api_caller._build_path(self.endpoint, sub_path=sub_path, query=query)
        return self.api_caller.get(path)

    def get_operator_flights(self, operator_id: str, start: Optional[str] = None, end: Optional[str] = None,
                              max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves recent and upcoming flights for a specific operator.

        Args:
            operator_id (str): The ICAO or IATA identifier for the operator.
            start (str): Optional, the starting date range for flight results in ISO8601 format.
            end (str): Optional, the ending date range for flight results in ISO8601 format.
            max_pages (int): Optional, the maximum number of pages to retrieve (default 1).
            cursor (str): Optional, a cursor for pagination (default None).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor
        }
        path = self.api_caller._build_path(self.endpoint, sub_path=f"{operator_id}/flights", query=query)
        return self.api_caller.get(path)