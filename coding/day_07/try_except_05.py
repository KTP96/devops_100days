### Missing File Error

try:
    with open("missingfile.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")