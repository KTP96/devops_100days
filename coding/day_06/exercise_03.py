"""Create a file named cpu.txt with:
45
82
91
67
Read each line, convert to integer, and print whether it is:
CRITICAL if >= 90
WARNING if >= 75
NORMAL otherwise
"""

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/cpu.txt", "w+") as file:
    file.write("45\n82\n91\n67\n")
    file.seek(0)
    for line in file:
        value=int(line)
        if value >=90:
            print("CRITICAL")
        elif value>=75:
            print("WARNING")
        else:
            print("NORMAL")

