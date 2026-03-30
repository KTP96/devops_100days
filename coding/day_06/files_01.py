### Opening the file

"""

"r" = read
"w" = write, overwrite
"a" = append
"w+" = write + read
"r+" = read + write
"a+" = append + read

"""

with open("/Users/tulasipravallikakatikireddy/Desktop/Learn/Scripts/day_06/servers.txt", "r") as file:
    context=file.read()
    print(context)