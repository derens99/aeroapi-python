from ..aeroapi_python.AeroAPI import AeroAPI

# Initialize the AeroAPI instance with your API key
api_key = 'your-api-key'
aero_api = AeroAPI(api_key)

# Get the flight route for a given flight ID
def get_flight_route(fa_flight_id='fa_flight_id'):
    flight_route = aero_api.history.flight_route(fa_flight_id)
    return flight_route

# Get the flight track for a given flight ID
def get_flight_track(fa_flight_id='fa_flight_id'):
    flight_track = aero_api.history.flight_track(fa_flight_id)
    return flight_track

# Get the last flight for a given aircraft registration
def get_last_flight(registration='registration'):
    last_flight = aero_api.history.last_flight(registration)
    return last_flight

# Get the flight information for a given flight ID
def get_flight_info(fa_flight_id='fa_flight_id'):
    flight_info = aero_api.history.flight_info(fa_flight_id)
    return flight_info