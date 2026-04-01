"""
line = "cache-1,67"
Parse it and handle missing memory value.
"""

line = "cache-1,67"
line=line.strip()
parts=line.split(",")

try:
    server=parts[0]
    cpu=int(parts[1])
    memory=(parts[2])
    print(f"{server} --> CPU: {cpu} --> Memory: {memory} ")
    
except IndexError:
    print("No memory value mentioned in line")