"""
Create a file named logs.txt with:

INFO: nginx started
WARNING: disk usage high
ERROR: database connection failed
INFO: backup completed

Read the file and print only lines that contain "ERROR".

"""

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/logs.txt", "w+") as file:
    file.write("INFO: nginx started\nWARNING: disk usage high\nERROR: database connection failed\nINFO: backup completed\n")
    file.seek(0)
    for line in file:
        line=line.strip()
        if "ERROR" in line:
            print(f"{line}")