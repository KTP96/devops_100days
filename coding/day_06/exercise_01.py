""" Create a file named regions.txt with:
us-west-2
us-east-1
eu-central-1
Read and print each line.

"""

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/regions.txt","w+") as file:
    file.write("us-west-2 \n")
    file.write("us-east-1 \n")
    file.write("eu-central-1 \n")
    file.seek(0)
    for line in file:
        print(line.strip())