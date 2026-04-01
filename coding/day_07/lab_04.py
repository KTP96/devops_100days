"""
Bad Parsed Line
"""

line="web-01,abc,60"
parts=line.split(",")

try:
    cpu=int(parts[1])
    memory=int(parts[2])
    print(cpu,memory)
except ValueError:
    print("CPU or Memory Value is not correct")
