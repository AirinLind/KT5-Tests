import allure
import pytest
from user_api import UserAPI
from store_api import StoreAPI
from schemas import UserModel, OrderModel
from config import BASE_URL


@allure.suite("User API Tests")
class TestUserAPI:
    user_api = UserAPI(BASE_URL)

    @allure.title("Test creating a user")
    def test_create_user(self):
        user_data = UserModel(
            id=123,
            username="testuser",
            firstName="Test",
            lastName="User",
            email="test@example.com",
            password="password",
            phone="1234567890",
            userStatus=1
        ).dict()

        response = self.user_api.create_user(user_data)
        assert response["code"] == 200

    @allure.title("Test getting user details")
    def test_get_user(self):
        response = self.user_api.get_user("testuser")
        user = UserModel(**response)
        assert user.username == "testuser"

    @allure.title("Test updating user details")
    def test_update_user(self):
        updated_data = {"firstName": "Updated", "lastName": "Name"}
        response = self.user_api.update_user("testuser", updated_data)
        assert response["code"] == 200

    @allure.title("Test deleting user")
    def test_delete_user(self):
        response = self.user_api.delete_user("testuser")
        assert response["code"] == 200


@allure.suite("Store API Tests")
class TestStoreAPI:
    store_api = StoreAPI(BASE_URL)

    @allure.title("Test placing an order")
    def test_place_order(self):
        order_data = OrderModel(
            id=1,
            petId=10,
            quantity=1,
            shipDate="2024-11-15T12:00:00Z",
            status="placed",
            complete=True
        ).dict()

        response = self.store_api.place_order(order_data)
        assert response["id"] == 1

    @allure.title("Test getting order details")
    def test_get_order(self):
        response = self.store_api.get_order(1)
        order = OrderModel(**response)
        assert order.id == 1

    @allure.title("Test deleting order")
    def test_delete_order(self):
        response = self.store_api.delete_order(1)
        assert response["code"] == 200

    @allure.title("Test getting inventory")
    def test_get_inventory(self):
        response = self.store_api.get_inventory()
        assert "sold" in response
