servers=[
    {"name":"web-01","cpu":90,"memory":78},
    {"name":"web-02","cpu":88,"memory":81}   
]

for server in servers:
    print(server["name"], server["cpu"], server["memory"])