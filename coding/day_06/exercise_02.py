"""
Create a file named services.txt with:

nginx
docker
ssh

Read and print:

Service: nginx
Service: docker
Service: ssh

"""

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/services.txt","w+") as file:
    file.write("nginx \n docker \n ssh \n")
    file.seek(0)
    for line in file:
        print(f"Service: {line.strip()}")