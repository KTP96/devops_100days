### file crash

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/servers.txt","r") as file:
    for line in file:
        line=line.strip()
        parts=line.split(",")
        try:
            cpu=int(parts[1])
        except:
            print("Invalid Number")

