"""
server_lines = [
    "web-01,45,60",
    "web-02,82,77",
    "db-1,91,88",
    "cache-1,67,72"
]

Each line means:
* server_name
* cpu
* memory

parse each line and convert cpu and memory to integers and use a function get_server_status(cpu, memory)
print:
web-01 --> CPU: 45% --> Memory: 60% --> NORMAL
web-02 --> CPU: 82% --> Memory: 77% --> WARNING
db-1 --> CPU: 91% --> Memory: 88% --> CRITICAL
cache-1 --> CPU: 67% --> Memory: 72% --> NORMAL

Status rules

* CRITICAL if cpu >= 90 or memory >= 90
* WARNING if cpu >= 75 or memory >= 75
* NORMAL otherwise

"""

def get_server_status(cpu, memory):
    if cpu>=90 or memory>=90:
        return "CRITICAL"
    elif cpu>=75 or memory>=75:
        return "WARNING"
    else:
        return "NORMAL"

server_lines = [
    "web-01,45,60",
    "web-02,82,77",
    "db-1,91,88",
    "cache-1,67,72"
]

for server in server_lines:
    server_data=server.split(",")
    server_name=server_data[0]
    cpu=int(server_data[1])
    memory=int(server_data[2])
    status=get_server_status(cpu,memory)
    print(f"{server_name} --> CPU: {cpu} --> Memory: {memory} --> {status}")