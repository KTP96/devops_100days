"""
Missing File
"""

try:
    with open("unknowfile.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File is not found")