"""
line = "db-01,91,88", Parse it into:
* server
* cpu
* memory and then print: db-01 --> CPU: 91 --> Memory: 88
"""

line = "db-01,91,88"
data=line.split(",")

server=data[0]
cpu=int(data[1])
memory=int(data[2])

print(f"Server: {server} \nCPU: {cpu}% \nMemory: {memory}%")