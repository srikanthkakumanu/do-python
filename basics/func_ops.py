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

def main():
    print(multiply(1, 2))
    print(add(1, 2, 3))
    print(add(1))
    print(add())
    print('pow: ', func_pow(2, 3))
    var_scope()

global_variable = 20

if __name__ == "__main__":
    main()
