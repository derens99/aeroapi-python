from ..aeroapi_python.AeroAPI import AeroAPI

# Initialize the AeroAPI instance with your API key
api_key = 'your-api-key'
aero_api = AeroAPI(api_key)

# Retrieves a list of operators
def get_all_operators():
    all_operators = aero_api.operators.get_all_operators()
    return all_operators

# Get the operator information for a given operator
def get_operator_info(operator_id='operator_id'):
    operator_info = aero_api.operators.get_operator_info(operator_id)
    return operator_info

# Get the canonical code for a given operator
def get_canonical_code(operator_id='operator_id'):
    canonical_code = aero_api.operators.get_canonical_code(operator_id)
    return canonical_code

# Get the flights for a given operator
def get_operator_flights(operator_id='operator_id'):
    operator_flights = aero_api.operators.get_operator_flights(operator_id)
    return operator_flights