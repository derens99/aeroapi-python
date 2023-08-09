from typing import Optional, Dict, Any
from aeroapi_python.APICaller import APICaller


class History:
    """
    A class for interacting with the OpenSky Network History API.

    Attributes:
        api_caller (APICaller): An instance of the `APICaller` class.
        endpoint (str): The API endpoint for history.

    Methods:
        __init__(self, api_caller: APICaller) -> None:
            Initializes a `History` instance.

        flight_map(self, flight_id: str, height: int = 480, width: int = 640, layer_on: Optional[str] = None,
                   layer_off: Optional[str] = None, show_data_block: Optional[bool] = None,
                   airports_expand_view: Optional[bool] = None, show_airports: Optional[bool] = None,
                   bounding_box: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves a map of a specific flight.

        flight_route(self, flight_id: str) -> Optional[Dict[str, Any]]:
            Retrieves the route of a specific flight.

        flight_track(self, flight_id: str, include_estimated_positions: Optional[bool] = None) -> Optional[Dict[str, Any]]:
            Retrieves the track of a specific flight.

        last_flight(self, registration: str) -> Optional[Dict[str, Any]]:
            Retrieves the last flight of a specific aircraft.

        flight_info(self, ident: str, ident_type: Optional[str] = None, start: Optional[int] = None,
                    end: Optional[int] = None, max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves information about a specific flight or set of flights.
    """

    def __init__(self, api_caller: APICaller) -> None:
        """
        Initializes a `History` instance.

        Args:
            api_caller (APICaller): An instance of the `APICaller` class.
        """
        self.api_caller = api_caller
        self.endpoint = 'history'

    def flight_map(self, flight_id: str, height: int = 480, width: int = 640, layer_on: Optional[str] = None,
                   layer_off: Optional[str] = None, show_data_block: Optional[bool] = None,
                   airports_expand_view: Optional[bool] = None, show_airports: Optional[bool] = None,
                   bounding_box: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves a map of a specific flight.

        Args:
            flight_id (str): The unique identifier of the flight.
            height (int): Optional, the height of the map in pixels (default 480).
            width (int): Optional, the width of the map in pixels (default 640).
            layer_on (str): Optional, a comma-separated list of layers to enable.
            layer_off (str): Optional, a comma-separated list of layers to disable.
            show_data_block (bool): Optional, whether to show the data block (default False).
            airports_expand_view (bool): Optional, whether to expand the view to include airports (default False).
            show_airports (bool): Optional, whether to show airports on the map (default False).
            bounding_box (str): Optional, a bounding box to restrict the map view.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {
            "height": height,
            "width": width,
            "layer_on": layer_on,
            "layer_off": layer_off,
            "show_data_block": show_data_block,
            "airports_expand_view": airports_expand_view,
            "show_airports": show_airports,
            "bounding_box": bounding_box,
        }
        path = self.api_caller._build_path(self.endpoint, sub_path=f"flights/{flight_id}/map", query=query)
        return self.api_caller.get(path)

    def flight_route(self, flight_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the route of a specific flight.

        Args:
            flight_id (str): The unique identifier of the flight.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        path = self.api_caller._build_path(self.endpoint, sub_path=f"flights/{flight_id}/route")
        return self.api_caller.get(path)

    def flight_track(self, flight_id: str, include_estimated_positions: Optional[bool] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves the track of a specific flight.

        Args:
            flight_id (str): The unique identifier of the flight.
            include_estimated_positions (bool): Optional, whether to include estimated positions (default False).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {"include_estimated_positions": include_estimated_positions}
        path = self.api_caller._build_path(self.endpoint, sub_path=f"flights/{flight_id}/track", query=query)
        return self.api_caller.get(path)

    def last_flight(self, registration: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the last flight of a specific aircraft.

        Args:
            registration (str): The registration of the aircraft.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        path = self.api_caller._build_path(self.endpoint, sub_path=f"aircraft/{registration}/last_flight")
        return self.api_caller.get(path)

    def flight_info(self, ident: str, ident_type: Optional[str] = None, start: Optional[int] = None,
                    end: Optional[int] = None, max_pages: int = 1, cursor: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about a specific flight or set of flights.

        Args:
            ident (str): The identifier of the flight or set of flights.
            ident_type (str): Optional, the type of identifier (default None).
            start (int): Optional, the start time of the search in seconds since epoch (default None).
            end (int): Optional, the end time of the search in seconds since epoch (default None).
            max_pages (int): Optional, the maximum number of pages to retrieve (default 1).
            cursor (str): Optional, a cursor for pagination (default None).

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {
            "ident_type": ident_type,
            "start": start,
            "end": end,
            "max_pages": max_pages,
            "cursor": cursor,
        }
        path = self.api_caller._build_path(self.endpoint, sub_path=f"flights/{ident}", query=query)
        return self.api_caller.get(path)