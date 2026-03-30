### Reading Line by Line

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/servers.txt","r") as file:
    for line in file:
        print(line)
        
       ## Each line often ends with \n, so usually use strip():
        print(line.strip())
        
