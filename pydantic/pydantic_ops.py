from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int

    def greet(user: User) -> str:
        return f"Hello, {user.name}!"

    def load(data: dict) -> User:
        return User.model_validate(data)
    
user = load({
    "id": 1,
    "name": "Alice",
    "age": 30
})
message = greet(user)
print(message)  # Output: Hello, Alice!