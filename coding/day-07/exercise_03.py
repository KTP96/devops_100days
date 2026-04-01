"""
Try opening a file called missing.txt.
If not found, print "File not found".

"""

try:
    with open("missing_file.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File is not found")