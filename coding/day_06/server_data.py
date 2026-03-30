"""

Create file servers.txt

web-01,45,60
web-02,82,77
db-1,91,88
cache-1,67,72

Requirements:

define function:
def get_server_status(cpu, memory):
open servers.txt
read line by line
for each line:
strip()
split(",")
extract server, cpu, memory
convert cpu and memory to int
get status from function

print:
web-01 --> CPU: 45% --> Memory: 60% --> NORMAL
web-02 --> CPU: 82% --> Memory: 77% --> WARNING
db-1 --> CPU: 91% --> Memory: 88% --> CRITICAL
cache-1 --> CPU: 67% --> Memory: 72% --> NORMAL

"""


def get_server_status(cpu,memory):
    if cpu>=90 or memory >=90:
        return("CRITICAL")
    elif cpu>=75 or memory >=75:
        return("WARNING")
    else:
        return("NORMAL")

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/servers.txt", "w+") as file:
    file.write("web-01,45,60\nweb-02,82,77\ndb-1,91,88\ncache-1,67,72")
    file.seek(0)
    for line in file:
        line=line.strip()
        parts=line.split(",")

        server=parts[0]
        cpu=int(parts[1])
        memory=int(parts[2])

        print(f"{server} --> CPU: {cpu}% --> Memory: {memory}% --> {get_server_status(cpu,memory)}")


        