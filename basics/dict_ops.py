person = {
    "name" : "Dave",
    "age" : 30,
    "job" : "Developer",
    (1,2,3): "Monte Carlo" # anything can be a key
}
print(person)
print(person['name'], person['age'], person['job'], person[(1,2,3)])

print(person.get('name'))
print(person.keys())
print(person.values())
print("age" in person.keys())

# Copy
copied_person = person.copy()
print(copied_person)

# Update
person["age"] = 35
person.update({"name": "Krishna", "age": 40})
print(person)

person.clear()
