servers=["web-prod-01","web-dev-01","db-prod-01"]

for server in servers:
    if "prod" in server:
        print(f"Production Servers Found : {server}")