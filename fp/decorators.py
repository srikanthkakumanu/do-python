# defining a decorator
def decor(funct):
    # wrapper function
    def wrap():
        print("Before function execution")
        funct()  # calling the original function
        print("After function execution")

    return wrap

# function to be decorated
def func():
    print("Inside the function!")


# applying the decorator
func = decor(func)

# calling the decorated function
func()