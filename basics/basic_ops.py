# String operations
greeting = "Hello World!"
print(greeting)

person = "John Doe"
greeting = "Hello,"
greeting_message = f"{greeting} {person}!"
print(greeting_message)

some_text = "   this is sample text    "
print(some_text.title())
print(some_text)
print(some_text.strip())
print(some_text.lstrip())
print(some_text.rstrip())
print(some_text.upper())
print(some_text.lower())
print(some_text.replace("sample", "test"))
print(some_text.find("sample"))
print(some_text.split(" ")) # splits the string into a list
# below is multi-line strings with special characters
print("""Hello World, This can't be a fake""")
url = "https://www.google.com"
print(url.removeprefix("https://"))
print(url.removesuffix(".com"))
print(url.removeprefix("https://").removesuffix(".com"))
print(url.startswith("https"))
print(url.endswith("com"))
print(url.find("google"))

# Number and Float operations
print(3*3)
print(3**3)
print(3.4/2)
print(22//2)
universe_age = 14_000_000_000
print(universe_age)
x, y, z = 1, 2, 3 # multiple assignment
print(x + y + z)

a = 17
b = 20.29
print(a + b)
print(a.is_integer())
print(a.as_integer_ratio())
print(a.bit_count())
print(a.__add__(34))
print(a.to_bytes(4, byteorder="little"))
print(a.to_bytes(4, byteorder="big"))
print(a.to_bytes(4, byteorder="big", signed=True))
print(a.to_bytes(4, byteorder="big", signed=False))
print(a.to_bytes(4, byteorder="big", signed=True).decode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=False).decode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=True).decode("utf-8").encode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=False).decode("utf-8").encode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=True).decode("utf-8").encode("utf-8").decode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=False).decode("utf-8").encode("utf-8").decode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=True).decode("utf-8").encode("utf-8").decode("utf-8").encode("utf-8"))
print(a.to_bytes(4, byteorder="big", signed=False).decode("utf-8").encode("utf-8").decode("utf-8").encode("utf-8"))
print(a.__and__(12))


z = 3 + 4j # complex number should end with j or J in Python
conj = z.conjugate()

print("Original:", z)       # 3+4j
print("Conjugate:", conj)   # 3-4j

# Integer methods
x = -10
print("Absolute value:", abs(x))
print("Integer from float:", int(5.9))
print("Power:", pow(2, 3))
print("Quotient & Remainder:", divmod(9, 4))

# Float methods
f = 5.0
print("Is integer:", f.is_integer())
print("As integer ratio:", 2.5.as_integer_ratio())
print("From hex:", float.fromhex('0x1.8p+1'))
print("To hex:", 3.0.hex())
print("Rounded value:", round(5.678, 2))

# Complex number methods
c = 3 + 4j
print("Complex number:", c)
print("Real part:", c.real)
print("Imaginary part:", c.imag)
print("Conjugate:", c.conjugate())

# Type conversions
print("Float from int:", float(3))
print("Complex from numbers:", complex(2, 3))
# Below is zen of python by Tim Peters
# import this
# print(this.s)

# Boolean operations
is_authenticated = True
is_admin = True
print(is_authenticated)
print(not is_authenticated)
x, y = 5, 10
print( x != 10)
print(is_admin and is_authenticated)
print(not is_admin and is_authenticated)
print(is_authenticated or is_admin)
# Truthy and Falsy
# Falsy
print(bool(0))
print(bool(""))
print(bool([]))
# Truthy
print(bool(1))
print(bool("Hello"))
print(bool([21, 32, 43]))