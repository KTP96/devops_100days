"""
Create a file named servers.txt with:

web-01,45,60
web-02,82,77
db-1,91,88

Read it and print:

web-01 --> CPU: 45 --> Memory: 60
web-02 --> CPU: 82 --> Memory: 77
db-1 --> CPU: 91 --> Memory: 88

"""

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/servers.txt", "w+") as file:
    file.write("web-01,45,60\nweb-02,82,77\ndb-1,91,88\n" )
    file.seek(0)
    for line in file:
        line=line.strip()
        parts=line.split(",")

        server=parts[0]
        cpu=parts[1]
        memory=parts[2]

        print(f"{server} --> CPU: {cpu} --> Memory: {memory}")