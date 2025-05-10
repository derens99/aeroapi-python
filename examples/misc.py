from ..aeroapi_python.AeroAPI import AeroAPI

# Initialize the AeroAPI instance with your API key
api_key = "your-api-key"
aero_api = AeroAPI(api_key)


# Get the owner of a given aircraft
def get_aircraft_owner(ident="ident"):
    aircraft_owner = aero_api.miscellaneous.aircraft_owner(ident)
    return aircraft_owner


# Get the aircraft type for a given aircraft type name
def get_aircraft_type(aircraft_type="aircraft_type"):
    aircraft_type = aero_api.miscellaneous.aircraft_type(aircraft_type)
    return aircraft_type


# Get the global disruption counts for a given entity type
def get_global_disruption_counts(entity_type="entity_type"):
    global_disruption_counts = aero_api.miscellaneous.global_disruption_counts(
        entity_type
    )
    return global_disruption_counts


# Get the disruption counts for a given entity
def get_disruption_counts(entity_type="entity_type", entity_id="entity_id"):
    disruption_counts = aero_api.miscellaneous.disruption_counts(entity_type, entity_id)
    return disruption_counts
