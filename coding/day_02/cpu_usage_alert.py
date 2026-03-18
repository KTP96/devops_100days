
servers=["web-01","web-02","db-1","cache-1"]
cpu_usages=[45,82,91,67]

for i in range(len(servers)):

    cpu = cpu_usages[i]
    server= servers[i]

    if cpu>=90:
        print(f"CRITICAL --> {server} --> {cpu}")

    elif cpu_usages[i]>=75:
        print(f"WARNING --> {server} --> {cpu}")
        
    else:
        print(f"NORMAL --> {server} --> {cpu}")

