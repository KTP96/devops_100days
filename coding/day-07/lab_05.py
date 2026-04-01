"""
Missing Field

"""

line="web-01,45"
parts=line.split(",")

try:
    cpu=int(parts[1])
    memory=int(parts[2])
    print(cpu,memory)

except IndexError:
    print("Missing Field in line")