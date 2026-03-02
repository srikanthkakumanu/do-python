# 1. Functions are first-class citizens
def func():
    print('I am function func()!')

func()
another_name = func # Create a new reference to func() named another_name, assign a function to a variable
another_name()
print("cat", func, 42) # can pass an argument
objects = ['cat', func, 42] # can store in data structures
print(objects[1])
dict = {'cat': 1, func: 2, 42: 3} # can store in data structures
var = dict[func]

# 2. Function composition: Pass function as argument
def inner():
    print("I am function inner()!")

def outer(inner):
    inner()

print(outer(inner))

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def hello():
    return 'Hello Stranger!'

def greet(funct):
    greeting = funct
    print(greeting)

greet(shout('dave'))  # pass function as an argument
greet(whisper('Joe'))  # pass function as an argument
greet(hello)  # pass function as an argument
greet(hello())  # pass function as value but not as an argument
