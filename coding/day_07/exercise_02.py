"""
Ask user for disk usage.
Use try/except so invalid input does not crash.

"""

try:
    disk_usage=int(input("Enter the disk usage: "))
    print(disk_usage)
except ValueError:
    print("Disk Usage must be number:")



