# Day 4 — Dictionaries

## **Dictionaries for real DevOps-style data**

- **Dictionary** stores data in **key : value** form.
- Ex:
```
server = {
    "name": "web-01",
    "cpu": 82,
    "memory": 68
}
```
Here:

* `"name"` is a key
* `"web-01"` is its value
* `"cpu"` is a key
* `82` is its value

- A **list** is good for ordered items.
- A **dictionary** is good for **named fields**.

---

## Why dictionaries matter in DevOps

- In real work, server data is not just one number.
- A server has:
  * hostname
  * IP
  * CPU
  * memory
  * disk
  * status
  * region
  * environment

- Dictionary helps keep related data together.
- Ex:
```
server = {
    "hostname": "web-prod-01",
    "ip": "10.0.0.5",
    "cpu": 76,
    "memory": 70,
    "env": "prod"
}
```
---

## Accessing dictionary values

```
server = {
    "name": "web-01",
    "cpu": 82,
    "memory": 68
}

print(server["name"])
print(server["cpu"])
print(server["memory"])
```
---

## Adding or updating values

```python
server = {
    "name": "web-01",
    "cpu": 82
}

server["memory"] = 70
server["cpu"] = 90

print(server)
```

---

## Looping through a dictionary

```python
server = {
    "name": "web-01",
    "cpu": 82,
    "memory": 68
}

for key in server:
    print(key, server[key])
```

Better style:

```python
for key, value in server.items():
    print(f"{key} --> {value}")
```

---

## List of dictionaries

```
servers = ["web-01", "web-02"]
cpu_usages = [45, 82]
```

```
servers = [
    {"name": "web-01", "cpu": 45},
    {"name": "web-02", "cpu": 82},
    {"name": "db-1", "cpu": 91},
    {"name": "cache-1", "cpu": 67}
]
```
- Each server keeps its own related data together.
- This is exactly how API data and cloud automation often looks.

---
