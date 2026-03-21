import httpx

# r = httpx.get(
#     "https://api.github.com/user",
#     auth=("user", "pass"),
# )

r = httpx.get("https://jsonplaceholder.typicode.com/todos")

print(r.status_code)
print(r.content)
print(r.headers["content-type"])
print(r.encoding)
print(r.text)
print(r.json())
