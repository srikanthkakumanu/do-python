# Object-Oriented Programming in Python

## Classes

- A class can have class-level attributes and instance-level attributes.
- Class-level attributes are shared by all instances of that class.
- Instance-level attributes are unique to each class object.
- We can delete the classes, inner classes, objects, methods, instance-level properties using `del` keyword.

## Constructor Overloading

- Constructor overloading is not **directly** supported in Python as it allows only one `__init__` method per class.
- However, it can be achieved by using:
  - Using default arguments/parameters
  - var-length arguments (*args, *kwargs)
  - Type checking inside the container

## self

- `self` refer to current object. I does not need to name as `self`, it can be any other name. But it is a standard convention to use `self`.

## Inheritance

- Python supports multiple inheritance.
- 