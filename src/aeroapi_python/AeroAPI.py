from aeroapi_python.Airports import Airports
from aeroapi_python.APICaller import APICaller
from aeroapi_python.Flights import Flights
from aeroapi_python.History import History
from aeroapi_python.Miscellaneous import Miscellaneous
from aeroapi_python.Operators import Operators


class AeroAPI:
    """
    A class for interacting with the FlightAware AeroAPI.

    Attributes:
        base_url (str): The base URL for the AeroAPI.
        api_key (str): The API key for the AeroAPI.
        api_caller (APICaller): An instance of the `APICaller` class.
        airports (Airports): An instance of the `Airports` class.
        operators (Operators): An instance of the `Operators` class.
        history (History): An instance of the `History` class.
        miscellaneous (Miscellaneous): An instance of the `Miscellaneous` class.
        flights (Flights): An instance of the `Flights` class.

    Methods:
        __init__(self, api_key: str) -> None:
            Initializes an `RWYAeroAPI` instance.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes an `RWYAeroAPI` instance.

        Args:
            api_key (str): The API key for the AeroAPI.
        """
        self.base_url = 'https://aeroapi.flightaware.com/aeroapi/'
        self.api_key = api_key
        self.api_caller = APICaller(self.base_url, self.api_key)
        self.airports = Airports(self.api_caller)
        self.operators = Operators(self.api_caller)
        self.history = History(self.api_caller)
        self.miscellaneous = Miscellaneous(self.api_caller)
        self.flights = Flights(self.api_caller)
