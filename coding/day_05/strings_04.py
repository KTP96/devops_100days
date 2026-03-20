### strings Split() and parsing

line="web_01,82,77"

parts=line.split(",")

print(parts)

server_name=parts[0]
cpu_usage=int(parts[1])
memory_usage=int(parts[2])

print(server_name)
print(cpu_usage)
print(memory_usage)