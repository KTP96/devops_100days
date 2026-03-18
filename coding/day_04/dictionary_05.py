## List of Dictionaries


servers=[
    {"name":"web-01","cpu":80},
    {"name":"web-02","cpu":78},
    {"name":"web-03","cpu":81}
]

print(servers)
print(len(servers))

for server in servers:
    if server["cpu"]>80:
        print(f"{server["name"]} --> {server["cpu"]}")