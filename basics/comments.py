"""
comments.py

This is a multi-line comment and Module level comment.
In Python, We two types of comments:
1. Single line comment: comment is started with #. 
    1.1 There is no concept called multi-line comments in Python. 
    1.2 We can use # to write multi-line comments.

2. docstrings: docstrings are stored at runtime in __doc__ attribute and help() function. 
    2.1 They start and end with """ """.
    2.2 We can use tools like Sphinx or pdoc to generate HTML 
    documentation from docstrings. 
    2.3 We have different styles such as  Google style, NumPy style, or reStructuredText.
    2.4 We can use ''' also for docstring or multi-line comments.
"""

class Calculator:
    """
    class-level comment: A simple calculator class to perform basic arithmetic operations
    """

    def add(self, a, b):
        """
        instance-level or method-level comment:
        Add two numbers and return the result.

        Parameters:
            a (int or float): The first number
            b (int or float): The second number
        Returns:
            int or float: The sum of the two numbers.
        """

        # inline comment, a comment that is started with # is not a docstring comment.
        return a + b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Parameters:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: Product of a and b.
        """

print(help(__name__)) # Returns the docstring of the module
print(__doc__) # Returns the docstring of the module
print(help(Calculator)) # Returns the docstring of the class
print(Calculator.__doc__) # Returns the docstring of the class
print(help(Calculator().add)) # Returns the docstring of the method
print(Calculator().add.__doc__) # Returns the docstring of the method

print(f"The Addition Result is {Calculator().add(1, 2)}")
