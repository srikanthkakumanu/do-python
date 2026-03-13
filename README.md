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

## Code Formatting and Linting

This project uses Ruff, a fast Python code formatter and linter designed as a drop-in replacement for Black. It ensures consistent code formatting while focusing on performance. For detailed instructions on using Ruff, see [Ruff Guide](docs/Ruff.md).

# Virtual Environments

Virtual environment can be installed using this command in a desired directory: `python3 -m venv .venv` 

A created virtual environment can be activated via: `source .venv/bin/activate` and it can be de-activated via `deactivate`.

We can freeze the environment and creating requirements.txt → `pip3 freeze > requirements.txt`

To use `requirements.txt`, we need to use this command after venv is installed and activated: `pip3 install -r requirements.txt`

Note: Make sure you select right environment based python interpreter. Homebrew (system) environment is different and .venv environment is different. Both use different pip3 environments to avoid conflicts or collision of packages.

