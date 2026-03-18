## Looping through a dictionary

server= {
    "name":"web-01",
    "cpu":90,
    "memory":80
}
for key in server:
    print(key,server[key])

## Better styling

for key in server:
    print(f"{key} --> {server[key]}")