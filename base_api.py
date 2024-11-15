import requests
from allure import step


class BaseAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    @step("Sending {method} request to {endpoint}")
    def send_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, **kwargs)
        with step("Response received"):
            step(f"Status Code: {response.status_code}")
            step(f"Response Body: {response.text}")
        response.raise_for_status()
        return response.json()
