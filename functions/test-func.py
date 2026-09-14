"""import requests
from typing import Optional, Dict, Any

class APIClient:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}


    def get(self, endpoint: str, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = requests.get(url, params=params, headers=self.headers)
        except requests.RequestException as e:
            raise RuntimeError(f"Network error: {e}") from e

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError("Resource not found")
        else:
            raise RuntimeError(f"Request failed with status {response.status_code}")

    def post(self, endpoint: str, data: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.post(url, json=data, headers=self.headers)
        except requests.RequestException as e:
            raise RuntimeError(f"Network error: {e}") from e

        if response.status_code == 201:
            return response.json()
        elif response.status_code == 400:
            raise ValueError("Bad request: invalid data")
        elif response.status_code == 409:
            raise ValueError("Conflict: resource already exists")
        else:
            raise RuntimeError(f"Request failed with status {response.status_code}")
"""

def get_valid_users(response):
    if response == None:
        return "error"
    try:
        return response.json()[datetime.fromisoformat("registered_at")]
    except KeyError:
        return "error"