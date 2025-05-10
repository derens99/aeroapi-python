from ..aeroapi_python.AeroAPI import AeroAPI

# Initialize the AeroAPI instance with your API key
api_key = 'your-api-key'
aero_api = AeroAPI(api_key)

# Search for flight and get
def get_flight(fa_flight_id='TESTID'):
    flight = aero_api.flights.get_flight(flight_id=fa_flight_id)
    return flight