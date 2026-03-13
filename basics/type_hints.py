"""
-- Type hints --

With Type hints, we can do static type checking in python.

Type hints in Python are a way to add type information to your code. They help with code.

Type hints allow you to specify the expected types of variables, function parameters, and return values
by adding type annotations.

Type hints are optional and do not affect the runtime behavior of your code, are not enforced at runtime
but can be checked using static type checkers

Type hints improve code readability and prevent incorrect usage.

Type Checking -> We can check the type of the code using this command: mypy script.py

"""
from typing import Optional, Union, Dict, List, TypedDict

# without type hints
def add(a, b):
    return a + b

# with type hints
def add(a: int, b: int) -> int:
    return a + b

x: int = 34
y: float = 34.5
z: str = "Hello"
flag: bool = True
nums: list[int] = [1, 2, 3]
contacts: dict[str, str] = {"name": "John"}
coords: tuple[int, int] = (1, 2)
result: None = None

# Type aliases
Vector: list[float] = [1.0, 2.0, 3.0]

# with optional and default parameters
def get_user_age(name: str, age: Optional[int] = None) -> str:
    if age:
        return f"{name} is {age} years old."
    return f"Age of {name} is unknown."


# If a function accepts multiple types, use "Union".
def process(value: Union[int, float]) -> float:
    return value * 2.5

# type hints for lists and dictionaries
def get_names(ages: Dict[str, int]) -> List[str]:
    return list(ages.keys())

# type hints with classes and methods
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# "TypedDict" helps define dictionaries with specific structures.
class Person(TypedDict):
    name: str
    age: int

person: Person = {"name": "Alice", "age": 30}

