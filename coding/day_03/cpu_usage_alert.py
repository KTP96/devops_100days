servers = ["web-01", "web-02", "db-1", "cache-1"]
cpu_usages = [45, 82, 91, 67]

def get_cpu_status(cpu):
    if cpu>=90:
        return "CRITICAL"
    elif cpu>=75:
        return "WARNING"
    else:
        return "NORMAL"

for i in range(len(servers)):
    server=servers[i]
    cpu=cpu_usages[i]
    status=get_cpu_status(cpu)
    print(f"Server: {server} has CPU of {cpu} --> {status}")