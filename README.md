# Python

This repository demonstrates the features of Python language and its capabilities.

## Installation

For detailed installation instructions, please refer to our comprehensive [Installation Guide](docs/Installation.md).

## Overview

- Python is a simple and general-purpose programming language.
- It is an interpreted language, which means that it is executed line by line.
- It is an object-oriented language, which means that it is based on the concept of objects.
- It is a dynamically typed language, which means that it does not require explicit type declarations.
- It is a high-level language, which means that it is easy to read and write.
- It is a multi-paradigm language, which means that it supports multiple programming paradigms.
- It is a cross-platform language, which means that it can run on any platform.
- By default, Python source files are treated as encoded in UTF-8.
- In interactive mode, the last printed expression is assigned to the variable `_`.
  - This variable should be treated as read-only by the user.
  - Don’t explicitly assign a value to it.
- Python supports functional programming paradigms, including higher-order functions, closures, and decorators. See [Functional Programming Guide](docs/FP.md) for detailed examples.
- Exception handling is covered in our [Exception Handling Guide](docs/Exceptions.md).
- **Type hints**: Static type checking is covered in our codebase using mypy and typing modules.
- Date and time operations is covered in our codebase using pendulum module.
- Simple prototype REST API using Bottle is covered in our codebase.
- URL based requests and JSON operations is covered in our codebase using urllib and requests modules.
- Rich text formatting is covered in our codebase using rich module.
- OpenWeatherMap API is covered in our codebase.
- Code formatting and linting is covered in our codebase using Ruff.
- Virtual environments are covered in our codebase using venv module and is covered in our [Virtual Environments Guide](docs/virtual_environments.md). 
- Package management is covered in our codebase using uv and is covered in [UV Guide](docs/uv.md).
- Async IO and Concurrency is covered in our codebase using asyncio module and is covered in [Concurrency Guide](docs/concurrency.md).

## Code Formatting and Linting

Ruff automatically format and lint the python code as per Python Style Guide i.e. Python Enhancement Proposal (PEP8). This project uses Ruff, a fast Python code formatter and linter designed as a drop-in replacement for Black. It ensures consistent code formatting while focusing on performance. Ruff advocates Python Style Guide (PEP8) indentation guidelines. For detailed instructions on using Ruff, see [Ruff Guide](docs/Ruff.md).

## Environment Variables and Using dotenv module

We can read environment variables using the `os` module: `os.environ.get('VARIABLE_NAME')`.

We can set environment variables via command line in your OS or programmatically by using:
`os.environ['VARIABLE_NAME'] = 'VALUE'`

We can unset environment variables using:
`del os.environ['VARIABLE_NAME']`

We can also use the `python-dotenv` module to read environment variables from a `.env` file. It is a Python package that loads environment variables from a `.env` file into the Python environment. The `.env` file should be placed in the root directory of the project. The `.env` file should contain one variable per line in the format `VARIABLE_NAME=VALUE`. This is an efficient way to manage environment variables in a Python script.

## Pydantic

Pydantic brings runtime data validation to Python using type hints.Pydantic v2 is covered in our codebase.

Pydantic in the Python ecosystem.

Pydantic is everywhere:

- FastAPI uses for request/response validation.
- Django Ninja uses Pydantic for API schemas.
- SQLModel combines Pydantic under the hook.
- Modern Python frameworks rely on Pyantic under the hood.


