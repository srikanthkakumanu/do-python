# decorators -> Add functionality to another function by wrapping it with additional logic
# decorator is a higher-order function as it takes a function as argument, returns a function

# defining a decorator Example-1
def decor(funct):
    # wrapper function
    def wrap():
        print("Before function execution")
        funct()  # calling the original function
        print("After function execution")
    return wrap

# defining a decorator Example-2
def just_move(funct):

    def wrapper():
        print('Preparing a move...')
        funct()
        print('move complete')
    return wrapper

@just_move # indicate it uses a decorator function just_move()
def stealth_attack():
    print("Performing a stealth attack")

# function to be decorated
@decor # indicate it uses decorator function decor()
def func():
    print("Inside the function!")

# applying the decorator
# func = decor(func)
# calling the decorated function
# func()

def main():
    stealth_attack()
    func()

if __name__ == "__main__":
    main()

# Real-world use of decorators
# --> @require_auth (check user auth before func conditionally runs
# --> @validate_input (check & validate func arguments before func runs
# --> @preprocess (modify func arguments to be in a specific format)