"""
Create a dictionary for one server with:
* name
* cpu
* memory
If cpu >= 80, print "High CPU" else print "CPU OK".

"""

server={
    "name":"server-01",
    "cpu":80,
    "memory":90
}

if server["cpu"]>=80:
    print("High CPU")
else:
    print("CPU OK")