"""
line = "nginx,active,80"
Use split(",") and print each part separately.
"""

line = "nginx,active,80"
data=line.split(",")

print(f"Application Name: {data[0]}")
print(f"Status: {data[1]}")
print(f"Port: {int(data[2])}")