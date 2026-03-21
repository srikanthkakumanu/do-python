import httpx

r = httpx.get("https://httpbin.org/get")
print(r.text)
r = httpx.get("https://httpbin.org/get", params={"key": "value"})
print(r.text)
r = httpx.get(
    "https://httpbin.org/get", params={"key": "value"}, headers={"X-Test": "true"}
)
print(r.text)
r = httpx.get(
    "https://httpbin.org/get",
    params={"key": "value"},
    headers={"X-Test": "true"},
    timeout=5.0,
)
print(r.text)

r = httpx.get("https://httpbin.org/get", auth=("user", "pass"))
print(r.text)

r = httpx.post("https://httpbin.org/post", data={"key": "value"})
print(r.text)
r = httpx.post("https://httpbin.org/post", json={"key": "value"})
print(r.text)

r = httpx.put("https://httpbin.org/put", data={"key": "value"})
print(r.text)
r = httpx.put("https://httpbin.org/put", json={"key": "value"})
print(r.text)

r = httpx.delete("https://httpbin.org/delete")
print(r.text)

r = httpx.head("https://httpbin.org/get")
print(r.text)

r = httpx.options("https://httpbin.org/get")
print(r.text)

r = httpx.patch("https://httpbin.org/patch", data={"key": "value"})
print(r.text)
r = httpx.patch("https://httpbin.org/patch", json={"key": "value"})
print(r.text)

r = httpx.request("GET", "https://httpbin.org/get")
print(r.text)
r = httpx.request("GET", "https://httpbin.org/get", params={"key": "value"})
print(r.text)

params = {"key": "value"}
headers = {"X-Test": "true"}
r = httpx.get("https://httpbin.org/get", params=params, headers=headers)
print(r.text)
