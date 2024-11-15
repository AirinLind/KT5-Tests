from base_api import BaseAPI


class UserAPI(BaseAPI):
    def create_user(self, user_data: dict):
        return self.send_request("POST", "user", json=user_data)

    def get_user(self, username: str):
        return self.send_request("GET", f"user/{username}")

    def update_user(self, username: str, user_data: dict):
        return self.send_request("PUT", f"user/{username}", json=user_data)

    def delete_user(self, username: str):
        return self.send_request("DELETE", f"user/{username}")
