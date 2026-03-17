name=input("Enter the server name :")
cpu=int(input("Enter CPU Usage"))
memory=float(input("Enter CPU Usage"))
is_healthy=True

print(name)
print(f"CPU Usage is {cpu}%")
print("Memory is", memory,"%")

if cpu>85:
    print("CPU is high")

else:
    print("CPU is Normal")

if is_healthy=="True" :
    print("Service is healthy")

else:
    print("Service is not healthy")