"""
line = "db-01,xyz,88"
Parse it and handle invalid integer conversion.
"""

from multiprocessing import Value


line = "db-01,dfsd23,88"
line=line.strip()
parts=line.split(",")

try:
    server=parts[0]
    cpu=int(parts[1])
    memory=int(parts[2])
    print(f"{server} --> CPU: {cpu} --> Memory: {memory}")
except ValueError:
    print("cpu and memory must be numbers")