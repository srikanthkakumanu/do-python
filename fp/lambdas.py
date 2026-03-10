# lambda functions are shorthand notation of defining a function.
from functools import reduce # reduce() is part of functools
from math import factorial

def basics():
    text = 'Hello World'
    reverse = lambda a: a[::-1] # Returns the characters in reverse order
    print(reverse)
    print(reverse(text))

    reverse = callable(lambda a: a[::-1]) # Prints True of False
    print(reverse)

    print((lambda a: a[::-1]) (text))

    # Average of three numbers
    print((lambda x, y, z: (x + y + z)) (10, 10, 10))
    print((lambda x, y, z: (x + y + z) / 3) (1.4, 1.1, 0.5))

    animals = ["ferret", "vole", "dog", "gecko"]
    print(sorted(animals, key = lambda a: -len(a)))

    """
    A lambda expression will typically have a parameter list, but it’s not required. 
    You can define a lambda function without parameters. The return value is then not dependent on any 
    input parameters.
    """
    forty_two_producer = lambda: 42
    print(forty_two_producer())

    # Conditional expressions
    print((lambda x: "even" if x % 2 == 0 else "odd")(2))
    print((lambda x: "even" if x % 2 == 0 else "odd")(3))

    def power_tuple(x):
        return x, x ** 2, x ** 3

    print(power_tuple(2))
    print(type(power_tuple(3)))
    # This below implicit tuple packing doesn't work
    # print((lambda x: x, x ** 2, x ** 3)(3))
    # But, the below statements will work
    print((lambda x: (x, x ** 2, x ** 3)) (3))
    print((lambda x: [x, x ** 2, x ** 3]) (3))
    print((lambda x: {1: x, 2: x ** 2, 3: x ** 3}) (3))

    # Using lambda within a f-string
    print(f"- {(lambda s: s[0:])('I am a string')} -")
    print(f"- {(lambda s: s[::-1])('I am a string')} -")

    # Sort the users by age
    random_list = [('Anna', 25), ('Paul', 40), ('Lisa', 10)]
    # Sort the list by age but not by name
    sorted_list = sorted(random_list, key=lambda user_tuple: user_tuple[1])
    print(sorted_list)

basics()

# map() operations
def maps():
    def reverse(s):
        return s[::-1]

    animals = ["cat", "dog", "hedgehog", "gecko"]

    i = map(reverse, animals) # 1
    print(list(i))

    i = map(reverse, animals) # 2
    for animal in i: print(animal)

    i = map(lambda s: s[::-1], animals) #3
    for animal in i: print(animal)

    print(list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"]))) # 4

    print("+".join(map(str, [1, 2, 3, 4, 5])))

# map() with multi iterators
def map_multi_iter():
    def add_three(a, b, c):
        return a + b + c

    print(list(map(add_three, [1, 2, 3], [10, 20, 30], [100, 200, 300])))

    print(
        list(
            map(
                lambda a, b, c: a + b + c,
                [1, 2, 3, 4],
                [10, 20, 30, 40],
                [100, 200, 300, 400],
            )
        )
    )

map_multi_iter()

# filter() operations
def filters():
    def greater_than_100(x):
        return x > 100

    print("filters: ",
        list(
            filter(
                greater_than_100,
                [1, 111, 2, 222, 3, 333]
            )
        )
    )
    print("filters: ", list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))

    print("Even: ", list(filter(lambda x: x % 2 == 0, range(10))))

    animals = ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]
    print(list(filter(lambda s: s.isupper(), animals)))

filters()

# reduce() operations
def reducer():
    print(reduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
    print(reduce((lambda x, y: x + y), range(1, 6)))
    # Or, simply use sum()
    print(sum([1, 2, 3, 4, 5]))

    print(reduce((lambda x, y: x + y), ["cat", "dog", "hedgehog", "gecko"]))
    # Or, simply use join()
    print("".join(["cat", "dog", "hedgehog", "gecko"]))

    # Factorial with reduce()
    def multiply(x, y): return x * y
    def factorial_with_reduce(n): return reduce(multiply, range(1, n + 1))
    def greater(x, y): return x if x > y else y

    print(factorial_with_reduce(6))
    # Or, simply use factorial()
    print(factorial(6))

    print(reduce(greater, [23, 49, 6, 32]))

    # (100 + 1 + 2 + 3 + 4 + 5) and 100 is initializer value
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100))
    # Or, sum()
    print(sum([1, 2, 3, 4, 5], start=100))

reducer()