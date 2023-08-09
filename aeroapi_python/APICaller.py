import logging
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urljoin

import requests


class APICaller:
    """
    A class for making API calls.

    Attributes:
        base_url (str): The base URL for the API.
        session (requests.Session): The session object for making requests.

    Methods:
        _send_request(method: str, endpoint: str, payload: Optional[Dict[str, Any]] 
         = None, headers: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
            Sends a request to the API.

        get(endpoint: str, headers: Optional[Dict[str, Any]] = None) -> 
        Optional[Dict[str, Any]]:
            Sends a GET request to the API.

        post(endpoint: str, payload: Dict[str, Any], headers: Optional[Dict[str, Any]]
          = None) -> Optional[Dict[str, Any]]:
            Sends a POST request to the API.

        _build_path(endpoint: str, sub_path: Optional[str]
          = None, query: Optional[Dict[str, Any]] = None) -> str:
            Builds a URL path for an API request.
    """

    def __init__(self, base_url: str, api_key: str) -> None:
        """
        Initializes the APICaller class.

        Args:
            base_url (str): The base URL for the API.
            api_key (str): The API key to use for authentication.
        """
        self.base_url = base_url

        self.session = requests.Session()
        self.session.headers.update({"x-apikey": api_key})

    def _send_request(
        self,
        method: str,
        endpoint: str,
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Sends a request to the API.

        Args:
            method (str): The HTTP method to use for the request.
            endpoint (str): The API endpoint (path).
            payload (dict): Optional, the data to send in the request body.
            headers (dict): Optional, headers to include in the request.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.request(method, url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(e)
            return None
        except ValueError as e:
            logging.error(e)
            return None

    def get(
        self, endpoint: str, headers: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Sends a GET request to the API.

        Args:
            endpoint (str): The API endpoint (path).
            headers (dict): Optional, headers to include in the request.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        return self._send_request("GET", endpoint, headers=headers)

    def post(
        self,
        endpoint: str,
        payload: Dict[str, Any],
        headers: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Sends a POST request to the API.

        Args:
            endpoint (str): The API endpoint (path).
            payload (dict): The data to send in the request body.
            headers (dict): Optional, headers to include in the request.

        Returns:
            dict: The parsed JSON response, or None if the request failed.
        """
        return self._send_request("POST", endpoint, payload, headers)

    def _build_path(
        self,
        endpoint: str,
        sub_path: Optional[str] = None,
        query: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Builds a URL path for an API request, including optional sub-path and query 
        parameters.

        Args:
            endpoint (str): The endpoint of the API request.
            sub_path (str): Optional, a sub-path to append to the endpoint.
            query (dict): Optional, a dictionary of query parameters to include in the 
            URL.

        Returns:
            str: The complete URL path for the API request.
        """
        path = f"{self.base_url}{endpoint}"
        if sub_path is not None:
            path += f"/{sub_path}"
        if query:
            filtered_query = {k: v for k, v in query.items() if v is not None}
            query_string = urlencode(filtered_query)
            path += f"?{query_string}"
        return path
