# use *args to accept any number of positional arguments
# using the argument with * is unpacked state and not using it is a packed state
# It returns a tuple
def print_total(*args):
    print(args) # return a tuple, packed state
    print(*args) # returns the numbers and not the tuple, unpacked state
    print(sum(args))

print_total(1, 2, 3, 4, 5, 6)
print_total(1, 2, 3, 4, 5, 6, 7)

# use **kwargs to accept any number of keyword arguments i.e. named arguments
# it returns dictionary
def print_kwargs(**kwargs):
    print(kwargs)
    print(*kwargs)
    print(**kwargs)

print_kwargs(name='yoshi', age=23)
print_kwargs(first_name='Maria', last_name='Don')
