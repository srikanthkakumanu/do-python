import httpx

# Client uses HTTP connection pooling and brings significant performance improvements compared to the standard library.
with httpx.Client() as client:
    response = client.get("https://www.httpbin.org/get")
    print(response.status_code)

with httpx.Client() as client:
    headers = {"User-Agent": "my-app/0.0.1"}
    response = client.get("https://www.httpbin.org/get", headers=headers)


print(response.status_code, response.json)

with httpx.Client(headers={"User-Agent": "my-app/0.0.1"}) as client:
    response = client.get("https://www.httpbin.org/get")

print(response.status_code, response.json)
print(response.json()["headers"]["User-Agent"])