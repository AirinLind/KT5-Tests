from base_api import BaseAPI


class StoreAPI(BaseAPI):
    def place_order(self, order_data: dict):
        return self.send_request("POST", "store/order", json=order_data)

    def get_order(self, order_id: int):
        return self.send_request("GET", f"store/order/{order_id}")

    def delete_order(self, order_id: int):
        return self.send_request("DELETE", f"store/order/{order_id}")

    def get_inventory(self):
        return self.send_request("GET", "store/inventory")
