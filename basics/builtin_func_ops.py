import asyncio


def abs_function():
    """
    Demonstrates the abs() function.
    Covers: absolute value of a number.
    """
    print("\n" + "=" * 60)
    print("1. ABS FUNCTION")
    print("=" * 60)

    # abs() function
    print("\n--- abs() Function Example ---")
    print(f"Absolute value of -3 is: {abs(-3)}")
    print(f"Absolute value of 2.5 is: {abs(2.5)}")

    # This function returns the absolute value of a number.
    # It is used to get the magnitude of a number,
    # magnitude means how far a number (either positive or negative) is from zero.
    # regardless of whether it is positive or negative.



async def async_generator():
    """
    An example of an asynchronous generator function.
    """
    yield 1
    await asyncio.sleep(1)
    yield 2
    await asyncio.sleep(1)
    yield 3


async def aiter_function():
    """
    Demonstrates the aiter() function.
    Covers: asynchronous iteration.
    """
    print("\n" + "=" * 60)
    print("2. aiter() FUNCTION")
    print("=" * 60)

    # aiter() function
    print("\n--- aiter() Function Example ---")
    iterator = aiter(async_generator())
    async for value in iterator:
        print(f"Value: {value}")
    print("Asynchronous iteration completed!")



def all_function():
    """
    Demonstrates the all() function.
    Covers: whether all elements in an iterable are true (evaluate to True).
    """
    print("\n" + "=" * 60)
    print("3. all() FUNCTION")
    print("=" * 60)

    # all() function
    print("\n--- all() Function Example ---")
    print(f"All numbers are even: {all(x % 2 == 0 for x in range(1, 11))}")
    print(f"All numbers are even: {all(x % 2 == 0 for x in range(10, 21))}")



async def anext_function():
    """
    Demonstrates the anext() function.
    Covers: get the next value from an asynchronous iterator.
    """
    print("\n" + "=" * 60)
    print("4. anext() FUNCTION")
    print("=" * 60)

    # anext() function
    print("\n--- anext() Function Example ---")
    iterator = aiter(async_generator())
    print(await anext(iterator))
    print(await anext(iterator))
    print(await anext(iterator))



def ascii_function():
    """
    Demonstrates the ascii() function.
    Covers: returns an integer representing the Unicode code point of a one-character string.
    """
    print("\n" + "=" * 60)
    print("5. ascii() FUNCTION")
    print("=" * 60)

    # ascii() function
    print("\n--- ascii() Function Example ---")
    print(f"Unicode code point for 'a' is: {ascii('a')}")
    print(f"Unicode code point for '😊' is: {ascii('😊')}")

    print(f"Unicode code point for 'Z' is: {ascii('Z')}")



def chr_function():
    """
    Demonstrates the chr() function.
    Covers: returns a string of one character whose Unicode code point is the integer i.
    """
    print("\n" + "=" * 60)
    print("6. chr() FUNCTION")
    print("=" * 60)

    # chr() function
    print("\n--- chr() Function Example ---")
    print(f"Character for Unicode code point 97 is: {chr(97)}")
    print(f"Character for Unicode code point 98 is: {chr(98)}")
    print(f"Character for Unicode code point 99 is: {chr(99)}")



def ord_function():
    """
    Demonstrates the ord() function.
    Covers: returns an integer representing the Unicode code point of a one-character string.
    """
    print("\n" + "=" * 60)
    print("7. ord() FUNCTION")
    print("=" * 60)

    # ord() function
    print("\n--- ord() Function Example ---")
    print(f"Unicode code point for 'a' is: {ord('a')}")
    print(f"Unicode code point for 'b' is: {ord('b')}")
    print(f"Unicode code point for 'c' is: {ord('c')}")



def bin_function():
    """
    Demonstrates the bin() function.
    Covers: returns a string representation of an integer in base 2.
    """
    print("\n" + "=" * 60)
    print("8. bin() FUNCTION")
    print("=" * 60)

    # bin() function
    print("\n--- bin() Function Example ---")
    print(f"Binary representation of 10 is: {bin(10)}")


def bool_function():
    """
    Demonstrates the bool() function.
    Covers: returns a bool value of an object.
    """
    print("\n" + "=" * 60)
    print("9. bool() FUNCTION")
    print("=" * 60)

    # bool() function
    print("\n--- bool() Function Example ---")
    print(f"Boolean value of an empty string is: {bool('')}")
    print(f"Boolean value of a non-empty string is: {bool('hello')}")
    print(f"Boolean value of an empty list is: {bool([])}")
    print(f"Boolean value of a non-empty list is: {bool([1, 2, 3])}")


def breakpoint_function():
    """
    Demonstrates the breakpoint() function.
    Covers: sets a breakpoint at the current position.
    """
    print("\n" + "=" * 60)
    print("10. breakpoint() FUNCTION")
    print("=" * 60)

    # breakpoint() function
    print("\n--- breakpoint() Function Example ---")
    breakpoint()


def bytearray_function():
    """
    Demonstrates the bytearray() function.
    Covers: creates a new bytearray object from an iterable or with a specified size.
    """
    print("\n" + "=" * 60)
    print("11. bytearray() FUNCTION")
    print("=" * 60)

    # bytearray() function
    print("\n--- bytearray() Function Example ---")
    byte_array = bytearray(b'hello')
    print(f"Byte array from a string: {byte_array}")
    print(f"Length of the byte array: {len(byte_array)}")


def bytes_function():
    """
    Demonstrates the bytes() function.
    Covers: returns a new bytes object from an iterable of integers.
    """
    print("\n" + "=" * 60)
    print("12. bytes() FUNCTION")
    print("=" * 60)

    # bytes() function
    print("\n--- bytes() Function Example ---")
    byte_array = bytes(b'hello')
    print(f"Bytes from a string: {byte_array}")
    print(f"Length of the bytes: {len(byte_array)}")



def zip_function():
    """
    Demonstrates the zip() function.
    Covers: returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences.
    """
    print("\n" + "=" * 60)
    print("13. zip() FUNCTION")
    print("=" * 60)

    # zip() function
    print("\n--- zip() Function Example ---")
    names = ['John', 'Jane', 'Alice']
    ages = [25, 30, 28]
    for name, age in zip(names, ages):
        print(f"Name: {name}, Age: {age}")

    # another zip() example
    x, y = [1, 2, 3], [4, 5, 6]
    zip_list = zip(x, y)
    for name, age in zip_list:
        print(f"Name: {name}, Age: {age}")
    # * operator unpacks the tuple / unzips the list
    x2, y2 = zip(*zip(x, y))
    print(x == list(x2), y == list(y2))



def slice_function():
    """
    Demonstrates the slice() function.
    Covers: returns a slice of a sequence.
    """
    print("\n" + "=" * 60)
    print("14. slice() FUNCTION")
    print("=" * 60)

    # slice() function
    print("\n--- slice() Function Example ---")
    sequence = "Hello, World!"
    print(f"Original sequence: {sequence}")
    print(f"Sliced sequence: {sequence[slice(6, None)]}")  # from start to end
    print(f"Sliced sequence: {sequence[slice(None, 5)]}")  # from start to index 4
    print(f"Sliced sequence: {sequence[slice(5, 12, 2)]}")  # from index 5 to index 11 step 2



def reversed_function():
    """
    Demonstrates the reversed() function.
    Covers: returns a reverse iterator over the values of the iterable.
    """
    print("\n" + "=" * 60)
    print("15. reversed() FUNCTION")
    print("=" * 60)

    # reversed() function
    print("\n--- reversed() Function Example ---")
    sequence = [1, 2, 3, 4, 5]
    print(f"Original sequence: {sequence}")
    for num in reversed(sequence):
        print(num)


def set_function():
    """
    Demonstrates the set() function.
    Covers: returns a set object from an iterable.
    """
    print("\n" + "=" * 60)
    print("16. set() FUNCTION")
    print("=" * 60)

    # set() function
    print("\n--- set() Function Example ---")
    sequence = [1, 2, 3, 2, 4, 4, 5]
    print(f"Original sequence: {sequence}")
    print(f"Set from sequence: {set(sequence)}")
    print(f"Convert list to set: {set(sequence)}")  # Note: set() converts list to set
    print(f"Type of set: {type(set(sequence))}")



def complex_function():
    """
    Demonstrates the complex() function.
    Covers: returns a complex number constructed from a real part and an optional imaginary part.
    """
    print("\n" + "=" * 60)
    print("17. complex() FUNCTION")
    print("=" * 60)

    # complex() function
    print("\n--- complex() Function Example ---")
    print(f"Complex number: {complex(3, 4)}")
    print(f"Real part: {complex(3, 4).real}")
    print(f"Imaginary part: {complex(3, 4).imag}")
    print("Creating complex number using string: +1.23")
    print(f"Complex number: {complex('+1.23')}")

    print("Creating complex number using string: -4.5j")
    print(f"Complex number: {complex('-4.5j')}")

    print("Creating complex number using string: -1.23+4.5j")
    print(f"Complex number: {complex('-1.23+4.5j')}")

    print("Creating complex number using string: ( -1.23+4.5J )")
    print(f"Complex number: {complex('\t( -1.23+4.5J )\n')}")

    print("Creating complex number using string: -Infinity+NaNj")
    print(f"Complex number: {complex('-Infinity+NaNj')}")

    print("Creating complex number using float: 1.23")
    print(f"Complex number: {complex(1.23)}")

    print("Creating complex number using imaginary part: imag=-4.5")
    print(f"Complex number: {complex(imag=-4.5)}")

    print("Creating complex number using real and imaginary parts: -1.23, 4.5")
    print(f"Complex number: {complex(-1.23, 4.5)}")

def main():
    abs_function()
    asyncio.run(aiter_function())
    all_function()
    # anext_function()
    ascii_function()
    chr_function()
    bool_function()
    # breakpoint_function()
    bytearray_function()
    bytes_function()
    ord_function()
    bin_function()
    zip_function()
    slice_function()
    reversed_function()
    set_function()
    complex_function()

# Run the demonstration if this file is executed directly
if __name__ == "__main__":
    main()