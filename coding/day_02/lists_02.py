"""
Looping through lists
Getting Lists Length
Adding itesm to a list
"""

from operator import le


servers=["web-01","web-02","db-01"]
print("Servers are : ")
for server in servers:
    print(server)

print(f"The count of servers is : {len(servers)}")

servers.append("db-02")
print(f"The count of servers is : {len(servers)}")

for server in servers:
    print(server)
    