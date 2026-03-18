"""
Dictionary helps keep related data together.

"""

server={
    "hostname":"web-prod-01",
    "ip_address":"10.0.0.5",
    "cpu":76,
    "memory":70,
    "env":"prod"
}

print(server)

## Accessing dictionary values.

print(server["hostname"])
print(server["ip_address"])
print(server["cpu"])
print(server["memory"])
print(server["env"])

