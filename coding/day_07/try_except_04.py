### File Parsing error

line="web-02,1bc,09"
parts=line.split(",")

try:
    cpu=int(parts[1])
    memory=int(parts[2])
    print(cpu,memory)
except ValueError:
    print("Bad Numeric Data in line")