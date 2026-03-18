### Store multiple server records using dictionaries and print health status for each server.

def get_server_status(cpu,memory):
    if cpu>=90 or memory>=90:
        return "CRITICAL"
    elif cpu>=75 or memory>=75:
        return "WARNING"
    else:
        return "NORMAL"

servers = [
    {"name": "web-01", "cpu": 45, "memory": 60},
    {"name": "web-02", "cpu": 82, "memory": 77},
    {"name": "db-1", "cpu": 91, "memory": 88},
    {"name": "cache-1", "cpu": 67, "memory": 72}
]

for server in servers:
    status=get_server_status(server["cpu"],server["memory"])
    print(f"{server["name"]} --> CPU: {server["cpu"]} --> Memory: {server["memory"]} --> {status}")