with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/servers.txt","r") as file:
    for line in file:
        line=line.strip()
        parts=line.split(",")
        
        server=parts[0]
        cpu=parts[1]
        memory=parts[2]

        print(f"Server: {server}\nCPU: {cpu}\nMemory: {memory} ")
        print("-------------")