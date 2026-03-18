"""
Checking if an item exists or not
"""

servers=["web-01","web-02","web-03","db-01"]

if "db-01" in servers:
    print("database server exisis")
else:
    print("No database server found!!")