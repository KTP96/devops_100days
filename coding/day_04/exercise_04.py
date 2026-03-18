"""
Create a list of dictionaries for 3 servers.
Each dictionary should have:
* name
* cpu
Loop through and print each server’s name and cpu.
"""

servers=[
    {"name":"web-01","cpu":89},
    {"name":"web-02","cpu":75},
    {"name":"web-03","cpu":68},
    {"name":"db-01","cpu":95},
    {"name":"db-02","cpu":64},

]

for server in servers:
    print(f"{server["name"]} --> {server["cpu"]}")
  

