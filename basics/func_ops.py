def multiply(a, b):
    return a * b

def add(a = 10, b = 20, c = 30):
    return a + b + c

def func_pow(value, pow):
    """
    This function raises the value to the power of pow.

    Parameters:
        value (int or float): The base number.
        pow (int or float): The exponent.

    Returns:
        int or float: The result of raising the base to the exponent.
    """
    return value ** pow #


# Variable Scope or Scope of variable
def var_scope():
    local_variable = 10
    print("local_variable value is : ", local_variable)
    print("global_variable value is :", global_variable )


def named_args(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

# We can return multiple value from a function, it returns a tuple
def return_multiple_values():
    return 10, "hello"

def main():
    print(multiply(1, 2))
    print(add(1, 2, 3))
    print(add(1))
    print(add())
    print('pow: ', func_pow(2, 3))
    var_scope()
    named_args(c=3, b=2, a=1) # we can pass arguments in any order as we are using named arguments approach
    print(return_multiple_values())
    print(*return_multiple_values())
    number, name = return_multiple_values()
    print(number, name)


global_variable = 20

if __name__ == "__main__":
    main()
