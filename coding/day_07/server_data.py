"""
Use this file data:

web-01,45,60
web-02,82,77
db-1,abc,88
cache-1,67
api-1,95,91

Write a script that:

writes this content to servers.txt
reads line by line
uses try/except
handles:
invalid integers
missing fields
prints valid lines as:
web-01 --> CPU: 45% --> Memory: 60% --> NORMAL
web-02 --> CPU: 82% --> Memory: 77% --> WARNING
api-1 --> CPU: 95% --> Memory: 91% --> CRITICAL
for bad lines print something like:
Skipping invalid line: db-1,abc,88
Skipping invalid line: cache-1,67

Use the same status function rules:

CRITICAL if cpu >= 90 or memory >= 90
WARNING if cpu >= 75 or memory >= 75
NORMAL otherwise

Send me your Day 7 code after you try it.
"""

def get_status(cpu,memory):
    if cpu>=90 or memory>=90:
        return "CRITICAL"
    elif cpu>=75 or memory>=75:
        return "WARNING"
    else:
        return "NORMAL"


with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_07/servers.txt","w+") as file:
    file.write("web-01,45,60\nweb-02,82,77\ndb-1,abc,88\ncache-1,67\napi-1,95,91")
    file.seek(0)
    for line in file:
        try:
            line=line.strip()
            parts=line.split(",")
            server=parts[0]
            cpu=int(parts[1])
            memory=int(parts[2])
            status=get_status(cpu,memory)

            print(f"{server} --> CPU: {cpu}% --> Memory: {memory}% --> {status}")
    
        except ValueError:
            print("CPU and memory values must be numbers")
            print(f"Skipping invalid line:{line}")
        except IndexError:
            print("server or cpu or memory value is missing")
            print(f"Skipping invalid line:{line}")

    


