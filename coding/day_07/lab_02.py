"""
User input to int

"""

try:
    cpu=int(input("Enter CPU:"))
    print(cpu)
except ValueError:
    print("CPU must be a valid number")