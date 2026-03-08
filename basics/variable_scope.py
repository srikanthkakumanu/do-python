x = 10
y = 20

def print_x():
    x = 5 # this is new local variable x, not the global variable x
    print('Local X: ', x)

def print_y():
    global y # Now y refers to global variable, it does not create a new local variable y
    y = 10
    print('Y: ', y)

print('Global X: ', x)
print('Global Y: ', y)
print_x()
print_y()
print('Global Y: ', y)

# scope within nested functions

def outer():
    age = 25

    def inner():
#        nonlocal age # nonlocal refers to nearest scope i.e. outer() method scope and not the global scope
        age = 35
        print(f'age inside inner() is: {age}')

    inner()
    print(f'age inside outer() is: {age}')

outer() # if we uncomment nonlocal stmt, then this value is 35 too.