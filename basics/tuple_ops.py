"""
Tuple
1. Tuple is an immutable list
2. Tuple is defined by using parentheses ()
3. Tuple is faster than list
"""

# Creating a tuple
dimensions = (1920, 1080)
print(dimensions[0])
print(dimensions[1])

# We can reassign a tuple, but we cannot change the values of tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuple with one element
my_t = (3,)
print(my_t)

# Tuple is faster than list
nums = tuple(num for num in range(0, 20, 3))
print(nums)

nums = tuple(num * 2 for num in range(0, 30))
print(nums)
