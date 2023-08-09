import pytest
from unittest.mock import patch, MagicMock
from aeroapi_python.APICaller import APICaller
import requests

def test_init():
    api_key = "sample_api_key"
    base_url = 'https://aeroapi.flightaware.com/aeroapi/'

    api_caller = APICaller(base_url, api_key)
    
    assert api_caller.base_url == 'https://aeroapi.flightaware.com/aeroapi/'
    assert api_caller.session.headers['x-apikey'] == api_key

@patch.object(APICaller, '_send_request')
def test_get(mocked_send_request):
    api_caller = APICaller('https://aeroapi.flightaware.com/aeroapi/', 'sample_api_key')
    api_caller.get("test_endpoint")
    mocked_send_request.assert_called_once_with("GET", "test_endpoint", headers=None)

@patch.object(APICaller, "_send_request")
def test_post(mocked_send_request):
    api_caller = APICaller("https://example.com/", "test_api_key")
    payload = {"key": "value"}
    api_caller.post("test_endpoint", payload, None)
    mocked_send_request.assert_called_once_with("POST", "test_endpoint", payload, None)

# Test building the URL path
@pytest.mark.parametrize(
    "endpoint, sub_path, query, expected",
    [
        ("endpoint", None, None, "https://example.com/endpoint"),
        ("endpoint", "sub", None, "https://example.com/endpoint/sub"),
        ("endpoint", "sub", {"key": "value", "key2": None}, "https://example.com/endpoint/sub?key=value"),
    ],
)
def test_build_path(endpoint, sub_path, query, expected):
    api_caller = APICaller("https://example.com/", "test_api_key")
    result = api_caller._build_path(endpoint, sub_path=sub_path, query=query)
    assert result == expected

# Test successful _send_request
@patch("aeroapi_python.APICaller.requests.Session.request")
def test_send_request_valid_response(mocked_request):
    api_caller = APICaller("https://example.com/", "test_api_key")
    mocked_response = MagicMock()
    mocked_response.json.return_value = {"status": "ok"}
    mocked_response.raise_for_status.return_value = None
    mocked_request.return_value = mocked_response

    result = api_caller._send_request("GET", "endpoint")
    assert result == {"status": "ok"}

@patch("aeroapi_python.APICaller.requests.Session.request")
def test_send_request_exception_raised(mocked_request):
    api_caller = APICaller("https://example.com/", "test_api_key")
    mocked_request.side_effect = requests.exceptions.RequestException("Test Exception")
    
    result = api_caller._send_request("GET", "endpoint")
    
    assert result is None

# Test _send_request with invalid JSON response
@patch("aeroapi_python.APICaller.requests.Session.request")
def test_send_request_invalid_json(mocked_request):
    api_caller = APICaller("https://example.com/", "test_api_key")
    mocked_response = MagicMock()
    mocked_response.json.side_effect = ValueError("Invalid JSON")
    mocked_response.raise_for_status.return_value = None
    mocked_request.return_value = mocked_response

    result = api_caller._send_request("GET", "endpoint")
    assert result is None