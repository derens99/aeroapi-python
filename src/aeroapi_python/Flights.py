from typing import Optional, Dict, Any, List, Tuple
from aeroapi_python.APICaller import APICaller


class Flights:
    """
    A class for interacting with the OpenSky Network Flights API.

    Attributes:
        api_caller (APICaller): An instance of the `APICaller` class.
        endpoint (str): The API endpoint for flights.

    Methods:
        __init__(self, api_caller: APICaller) -> None:
            Initializes a `Flights` instance.

        get_flight(self, flight_id: str) -> Optional[Dict[str, Any]]:
            Retrieves information about a specific flight.

        get_all_states(self, time: int = None, icao24: Optional[str] = None) -> Optional[Dict[str, Any]]:
            Retrieves the state vectors of all aircraft.

        get_states(self, time: int = None, icao24s: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
            Retrieves the state vectors of specific aircraft.

        search_flights(self, operators: List[Tuple[str, Any]]) -> Optional[Dict[str, Any]]:
            Searches for flights based on specified criteria.

        count_search_flights(self, operators: List[Tuple[str, Any]]) -> Optional[Dict[str, Any]]:
            Counts the number of flights that match specified criteria.

        search_flights_positions(self, operators: List[Tuple[str, Any]]) -> Optional[Dict[str, Any]]:
            Searches for flights and returns their positions.

        print_search_query_keys() -> None:
            Prints the available query keys for `search_flights`.
    """

    def __init__(self, api_caller: APICaller) -> None:
        """
        Initializes a `Flights` instance.

        Args:
            api_caller (APICaller): An instance of the `APICaller` class.
        """
        self.api_caller = api_caller
        self.endpoint = "flights"

    def get_flight(self, flight_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves information about a specific flight.

        Args:
            flight_id (str): The unique identifier of the flight.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, flight_id)
        )

    def get_all_states(
        self, time: Optional[int] = None, icao24: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves the state vectors of all aircraft.

        Args:
            time (int): Optional, the time of the request in seconds since epoch.
            icao24 (str): Optional, the ICAO 24-bit address of the aircraft.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {}
        if time is not None:
            query["time"] = time
        if icao24 is not None:
            query["icao24"] = icao24
        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, "all", query)
        )

    def get_states(
        self, time: Optional[int] = None, icao24s: Optional[List[str]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves the state vectors of specific aircraft.

        Args:
            time (int): Optional, the time of the request in seconds since epoch.
            icao24s (List[str]): Optional, a list of ICAO 24-bit addresses of the aircraft.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query = {}
        if time is not None:
            query["time"] = time
        if icao24s is not None:
            query["icao24"] = ",".join(icao24s)
        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, "states", query)
        )

    def search_flights(
        self, operators: List[Tuple[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """
        Searches for flights based on specified criteria.

        Args:
            operators (List[Tuple[str, Any]]): A list of tuples representing the search criteria.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query_string = ""
        for op, args in operators:
            if op in {"false", "true", "null", "notnull"}:
                query_string += f"{{{op} {args}}}"
            elif op in {
                "=",
                "!=",
                "<",
                ">",
                "<=",
                ">=",
                "match",
                "notmatch",
                "range",
                "in",
                "orig_or_dest",
                "airline",
                "aircraftType",
                "ident",
                "ident_or_reg",
            }:
                if isinstance(args, (list, tuple, set)):
                    args_str = " ".join(map(str, args))
                else:
                    args_str = str(args)
                query_string += f"{{{op} {args_str}}}"

        query = {"query": query_string}

        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, "search", query)
        )

    def count_search_flights(
        self, operators: List[Tuple[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """
        Counts the number of flights that match specified criteria.

        Args:
            operators (List[Tuple[str, Any]]): A list of tuples representing the search criteria.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query_string = ""
        for op, args in operators:
            if op in {"false", "true", "null", "notnull"}:
                query_string += f"{{{op} {args}}}"
            elif op in {
                "=",
                "!=",
                "<",
                ">",
                "<=",
                ">=",
                "match",
                "notmatch",
                "range",
                "in",
                "orig_or_dest",
                "airline",
                "aircraftType",
                "ident",
                "ident_or_reg",
            }:
                if isinstance(args, (list, tuple, set)):
                    args_str = " ".join(map(str, args))
                else:
                    args_str = str(args)
                query_string += f"{{{op} {args_str}}}"

        query = {"query": query_string}

        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, "search/count", query)
        )

    def search_flights_positions(
        self, operators: List[Tuple[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """
        Searches for flights and returns their positions.

        Args:
            operators (List[Tuple[str, Any]]): A list of tuples representing the search criteria.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        query_string = ""
        for op, args in operators:
            if op in {"false", "true", "null", "notnull"}:
                query_string += f"{{{op} {args}}}"
            elif op in {
                "=",
                "!=",
                "<",
                ">",
                "<=",
                ">=",
                "match",
                "notmatch",
                "range",
                "in",
                "orig_or_dest",
                "airline",
                "aircraftType",
                "ident",
                "ident_or_reg",
            }:
                if isinstance(args, (list, tuple, set)):
                    args_str = " ".join(map(str, args))
                else:
                    args_str = str(args)
                query_string += f"{{{op} {args_str}}}"

        query = {"query": query_string}

        return self.api_caller.get(
            self.api_caller._build_path(self.endpoint, "search/positions", query)
        )

    @staticmethod
    def print_search_query_keys() -> None:
        """
        Prints the available query keys for `search_flights`.
        """
        print("Available query keys for search_flights:\n")
        print(
            "-prefix STRING              Prefix of aircraft ident (e.g., N for US registrations)"
        )
        print(
            "-type STRING                Aircraft type with wildcards (e.g., B73* for all Boeing 737 variants)"
        )
        print("-idents STRING              Aircraft ident with wildcards")
        print(
            "-identOrReg STRING          Aircraft ident or registration with wildcards"
        )
        print("-airline STRING             Airline/operator ident with wildcards")
        print("-destination STRING         ICAO or IATA code of destination airport")
        print("-origin STRING              ICAO or IATA code of origin airport")
        print(
            "-originOrDestination STRING ICAO or IATA code of origin or destination airport"
        )
        print("-aboveAltitude INTEGER      Minimum altitude in feet")
        print("-belowAltitude INTEGER      Maximum altitude in feet")
        print("-aboveGroundspeed INTEGER   Minimum groundspeed in knots")
        print("-belowGroundspeed INTEGER   Maximum groundspeed in knots")
        print(
            '-latlong "MINLAT MINLON MAXLAT MAXLON"  Latitude/longitude box for filtering flights'
        )
        print(
            "-filter {ga|airline}        Filter by general aviation or airline flights"
        )
