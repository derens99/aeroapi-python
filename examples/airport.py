import os
from aeroapi_python.AeroAPI import AeroAPI

# Initialize the AeroAPI instance with your API key
api_key = 'your-api-key'
aero_api = AeroAPI(api_key)

# Get a list of all airports
def get_airports():
    airports = aero_api.airports.get_airports()
    return airports

# Get information about a specific airport by code
def get_airport_info(airport_code='KLAX'):
    airport_info = aero_api.airports.get_airport(airport_code)
    return airport_info

# Get the canonical name of an airport by code
def get_airport_canonical(airport_code='KLAX'):
    airport_canonical = aero_api.airports.get_canonical(airport_code)
    return airport_canonical

# Get a list of airports with delays
def get_airports_with_delays():
    airports_with_delays = aero_api.airports.get_airports_with_delays()
    return airports_with_delays

# Get a list of all flights at a specific airport
def get_all_airport_flights(airport_code='KLAX'):
    all_airport_flights = aero_api.airports.all_flights(airport_id=airport_code)
    return all_airport_flights

# Get a list of recent arrivals at a specific airport
def get_arrivals(airport_code='KLAX'):
    arrivals = aero_api.airports.recent_arrivals(airport_id=airport_code)
    return arrivals

# Get a count of flights at a specific airport
def get_counts(airport_code='KLAX'):
    counts = aero_api.airports.get_counts(airport_id=airport_code)
    return counts

# Get a list of recent departures from a specific airport
def get_departures(airport_code='KLAX'):
    departures = aero_api.airports.recent_departures(airport_id=airport_code)
    return departures

# Get a list of scheduled arrivals at a specific airport
def get_scheduled_arrivals(airport_code='KLAX'):
    scheduled_arrivals = aero_api.airports.scheduled_arrivals(airport_id=airport_code)
    return scheduled_arrivals

# Get a list of scheduled departures from a specific airport
def get_scheduled_departures(airport_code='KLAX'):
    scheduled_departures = aero_api.airports.scheduled_departures(airport_id=airport_code)
    return scheduled_departures

# Get a list of flights between two airports
def get_flights_between_airports(origin='KLAX', destination='KJFK'):
    flights_between_airports = aero_api.airports.get_flights_between_airports(
        origin_id=origin, dest_id=destination)
    return flights_between_airports

# Get a list of nearby airports based on latitude and longitude
def get_nearby_airports(airport_code='KLAX', radius=10):
    nearby_airports = aero_api.airports.get_nearby_airports(
        airport_id=airport_code, radius=radius)
    return nearby_airports
