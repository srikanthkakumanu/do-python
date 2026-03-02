## Table of Contents

- [1.1 Pure Functions](#11-pure-functions)
- [1.2 Functions are first-class citizens and Higher-Order](#12-functions-are-first-class-citizens-and-higher-order)
  - [1.2.1 Function composition: Pass functions as arguments](#121-function-composition-pass-functions-as-arguments)
  - [1.2.2 Higher-Order functions](#122-higher-order-functions)
    - [1.2.2.1 Closure](#1221-closure)
    - [1.2.2.2 Decorator](#1222-decorator)
- [1.3 Recursion](#13-recursion)

<div style="text-align: justify;">

# 1. Functional Programming Paradigm and Lambda functions

In Python, Everything is an Object. Thus, a function type is also an Object.

Any functional programming language should follow the following concepts.

- Pure Functions
- Functions are first-class and can be higher-order
- Variables are immutable
- Recursion

## 1.1 Pure Functions 

A **pure function** is a function whose output value follows solely from its input values without any observable side 
effects. Computation proceeds by nested or composed function calls without changes to state or mutable data.

- A pure function is **immutable**. It does not change or modify any argument or global variables and no hidden I/O.
- **No side effects** - It always produces the same output for the same input values

Therefore, a **pure function** is **deterministic**.


## 1.2 Functions are first-class citizens and Higher-Order

In Python, functions are first-class citizens/variables. They have same characteristics as values like strings and numbers.

- We can assign a function to a variable. We can use that variable the same way we would use the function itself.
- A function can be passed to other functions as a parameter. This is called **Function composition**. These functions are called **Higher-Order**.
- A function can return another function. These functions are called **Higher-Order**. 
- A function can be stored in data structures (such as lists, maps, dictionaries) as a value.
- There are built-in higher-order functions such as `sorted(), filter(), map()`

### 1.2.1 Function composition: Pass functions as arguments

We can pass the function object as an argument. Please note, If we called the function object with parenthesis, 
then we wouldn't pass the function object but instead its return value.

**Note:** Python provides a shorthand notation called a **decorator** to facilitate wrapping one function inside another.

```python
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

    
```

### 1.2.2 Higher-Order functions

A **Higher-Order** function:
- A function can be passed to other functions as a parameter. This is also called — **Function composition**.
- A function can return another function.
- There are built-in higher-order functions such as `sorted(), filter(), map()`
- In FP paradigm — ***closures***, ***decorators*** and ***callbacks*** improve the code modularity, reusability and abstraction.

#### 1.2.2.1 Closure

**Closure** — Closures allow functions to remember and use variables from parent scope even after parent function has finished running.
This makes essential them for **Higher-Order** functions.

Closure Example:
```python
def counter(start=0):  # higher order function
    count = start 
    
    def increment():  # inner function
        nonlocal count  # retains access to 'count' even after counter() ends
        count += 1
        return count
    
    return increment  # returns the inner function

counter1 = counter(5)  # closure retains count = 5
print(counter1())  
print(counter1())  

counter2 = counter(10)  # new closure with count = 10
print(counter2())
```
#### 1.2.2.2 Decorator

**Decorator** — Decorators extend or modify functions without changing their original code by wrapping them inside another function.
They enhance **Higher-Order** functions by enabling tasks like caching results, transforming I/O, tracking function calls, controlling access etc.

Decorator Example:

```python
# defining a decorator 
def decor(func):  
    
    # wrapper function 
    def wrap():  
        print("Before function execution")  
        func()  # calling the original function  
        print("After function execution")  
    return wrap  
  
# function to be decorated  
def func():  
    print("Inside the function!")  
  
# applying the decorator  
func = decor(func)  
  
# calling the decorated function  
func()
```
## 1.3 Recursion

In FP paradigm, no **for-loop** or **while-loop**. Instead, it uses recursion. Recursion is a process in which a function
calls itself directly or indirectly.

</div>
