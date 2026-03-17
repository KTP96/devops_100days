"""
Python script that checks the health of a server based on CPU and memory usage
The script should:

Inputs :
server name
CPU usage
memory usage

Output :
server details
health status:
"""

server_name=input("Enter the server name:")
cpu_usage=int(input("Enter the CPU Usage:"))
memory_usage=int(input("Enter the Memory Usage:"))

print("\n--- Server Health Report ---")
print(f"Server Name is {server_name}")
print(f"CPU Usage is {cpu_usage}")
print(f"Memory Usage is {memory_usage}")

if cpu_usage>85 or memory_usage>90:
    print("Health Status: CRITICAL")
elif cpu_usage>70 or memory_usage>75:
    print("Health Status: WARNING")
else:
    print("Health Status: HEALTHY")
