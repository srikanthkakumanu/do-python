from typing import List, Optional
from pydantic import BaseModel


class Food(BaseModel):
    name: str
    price: float
    ingredients: Optional[List[str]] = None


class Restaurant(BaseModel):
    name: str
    location: str
    foods: List[Food]


restaurant = Restaurant(
    name="Tasty Bites",
    location="123 Main St",
    foods=[
        {
            "name": "Pizza",
            "price": 9.99,
            "ingredients": ["dough", "cheese", "tomato sauce"],
        },
        {
            "name": "Burger",
            "price": 7.99,
            "ingredients": ["bun", "chicken patty", "lettuce", "tomato"],
        },
    ],
)

print(restaurant)
print(restaurant.model_dump)
