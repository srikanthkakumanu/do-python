# F-String Examples

# Old approach
message = "Hello"
name = "World"
print("{} {}".format(message, name))
print("{0} {1}".format(message, name))
print("{x} {y}".format(x=message, y=name))

# New approach
print(f"{'Hello'}{'World'}")

# Expressions in f-strings
x = 5
y = 6
print(f"{x*y} is the result of {x} multiplied by {y}")

# Multiple expressions in f-strings
print(f"{3*10} is the result of {3} multiplied by {10}")