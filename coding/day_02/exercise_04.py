"""
Given this list:

hostnames = ["app-prod-1", "app-dev-1", "db-prod-1", "db-test-1"]

Print only the production servers.

"""

hostnames=["app-prod-1", "app-dev-1", "db-prod-1", "db-test-1"]

print("The Production Servers are: ")
for hostname in hostnames:
    if "prod" in hostname:
        print(hostname)