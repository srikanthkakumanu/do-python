# Exception Handling
<div class="style=div">

## Basic Exception Handling Skeleton

```
try:
  # code
except:
  # code
finally:
  # code
```

## Exception Hierarchy

All built-in exceptions in Python inherit from a base class called `BaseException`. All exception and warning classes inherit from `BaseExeption`.
`BaseException` has two more important base subclasses: `Exception` and `Warning`.
The subclasses of `BaseException` are either internal to Python or deprecated. Therefore, we concern only with subclasses of `Exception`.

## Exception Inheritance Hierarchy (Simplified View)

```
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
     +-- StopIteration
     +-- StopAsyncIteration
     +-- ArithmeticError
     |    +-- FloatingPointError
     |    +-- OverflowError
     |    +-- ZeroDivisionError
     +-- AssertionError
     +-- AttributeError
     +-- BufferError
     +-- EOFError
     +-- ImportError
     +-- LookupError
     |    +-- IndexError
     |    +-- KeyError
     +-- MemoryError
     +-- NameError
     |    +-- UnboundLocalError
     +-- OSError
     |    +-- BlockingIOError
     |    +-- ChildProcessError
     |    +-- ConnectionError
     |    |    +-- BrokenPipeError
     |    |    +-- ConnectionAbortedError
     |    |    +-- ConnectionRefusedError
     |    |    +-- ConnectionResetError
     |    +-- FileExistsError
     |    +-- FileNotFoundError
     |    +-- InterruptedError
     |    +-- IsADirectoryError
     |    +-- NotADirectoryError
     |    +-- PermissionError
     |    +-- ProcessLookupError
     |    +-- TimeoutError
     +-- ReferenceError
     +-- RuntimeError
     |    +-- NotImplementedError
     |    +-- RecursionError
     +-- SyntaxError
     |    +-- IndentationError
     |         +-- TabError
     +-- SystemError
     +-- TypeError
     +-- ValueError
     |    +-- UnicodeError
     |         +-- UnicodeDecodeError
     |         +-- UnicodeEncodeError
     |         +-- UnicodeTranslateError
     +-- Warning
          +-- DeprecationWarning
          +-- PendingDeprecationWarning
          +-- RuntimeWarning
          +-- SyntaxWarning
          +-- UserWarning
          +-- FutureWarning
          +-- ImportWarning
          +-- UnicodeWarning
          +-- BytesWarning
          +-- ResourceWarning
         
```

## Handling Exceptions

Multiple exceptions can be handled together by specifying them in a tuple:

```
except (ValueError, TypeError) as e:
  # Handle TypeError and ValueError
```

We can use an optional `else` clause after all `except` blocks. The code in `else` will only execute if no exceptions were raised in the `try` block.
This can be useful to run code that should only execute if everything in the `try` block succeeded.

```
try:
  # Code
except:
  # Exception occurred

else:
  # No exceptions
  pass
```

## Best Practices for handling exceptions

Here are some best practices to keep in mind when dealing with exceptions in Python:


- Avoid broad `except` clauses that catch all exceptions. Be as specific as possible when handling expected error conditions.

- Document all exceptions that can be raised from a function or module using docstrings and comments.

- Only catch exceptions that you know how to handle. Propagate unexpected ones to the caller.

- Print the exception traceback for debugging but provide a user-friendly error message in production.

- Use custom exception classes to indicate specific error conditions relevant to your domain.

- Perform cleanup actions like closing files and releasing resources in a `finally` block.

- Use the `with` statement for resource handling instead of explicit `try`/`finally`.

- Raise exceptions at the source of the error rather than letting issues propagate up.

- Limit use of bare raise statements to reraising caught exceptions.

</div>