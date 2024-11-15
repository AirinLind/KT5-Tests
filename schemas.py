from pydantic import BaseModel, Field
from typing import Optional


class UserModel(BaseModel):
    id: int
    username: str
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    userStatus: Optional[int]


class OrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: Optional[str]
    status: str = Field(..., regex="^(placed|approved|delivered)$")
    complete: bool
