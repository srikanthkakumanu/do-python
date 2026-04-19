# https://github.com/Coding-Crashkurse/Pydantic-v2-crashcourse/blob/main/code.ipynb
# https://www.youtube.com/watch?v=7aBRk_JP-qY
from typing import List, Any
from pydantic import (
    BaseModel,
    EmailStr,
    PositiveInt,
    conlist,
    Field,
    HttpUrl,
    field_validator,
    model_validator,
)


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class Employee(BaseModel):
    id: PositiveInt
    name: str
    email: EmailStr
    age: int = Field(..., gt=18, lt=65)
    website: HttpUrl
    skills: conlist(str, min_items=1)


class Owner(BaseModel):
    name: str
    email: EmailStr

    @model_validator(mode="before")
    @classmethod
    def check_sensitive_info_exposure(cls, data: Any) -> Any:

        if isinstance(data, dict):
            if "password" in data:
                raise ValueError(
                    "Sensitive information exposure: 'password' field is not allowed"
                )
            if "card_number" in data:
                raise ValueError(
                    "Sensitive information exposure: 'card_number' field is not allowed"
                )
        return data

    @model_validator(mode="after")
    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if " " not in v:
            raise ValueError("Owner name must contain a space")
        return v.title()


class Restaurant(BaseModel):
    name: str = Field(..., pattern=r"^[A-Za-z0-9' ]+$")
    owner: Owner
    address: Address
    employees: conlist(Employee, min_items=1)
    number_of_seats: PositiveInt
    delivery: bool
    website: HttpUrl


# Creating an instance of the Restaurant class
restaurant_instance = Restaurant(
    name="Tasty Bites",
    owner={"name": "John Doe", "email": "john.doe@example.com"},
    address={
        "street": "123, Flavor Street",
        "city": "Tastytown",
        "state": "TS",
        "zip_code": "12345",
    },
    employees=[
        {"name": "Jane Doe", "position": "Chef", "email": "jane.doe@example.com"},
        {"name": "Mike Roe", "position": "Waiter", "email": "mike.roe@example.com"},
    ],
    number_of_seats=50,
    delivery=True,
    website="http://tastybites.com",
)

# Printing the instance
print(restaurant_instance)

try:
    owner_instance = Owner(name="JohnDoe", email="john.doe@example.com")
except ValueError as e:
    print(e)


print(Owner(name="John Doe", email="john.doe@example.com", password="password123"))

try:
    Owner(name=123, email="john.doe@example.com", password="password123")
except ValueError as e:
    print(e)
