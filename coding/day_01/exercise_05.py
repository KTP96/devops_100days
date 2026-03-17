cpu=int(input("Enter the CPU: "))
if cpu >=90:
    print("Critical")
elif cpu >=75:
    print("Warning")
else:
    print("Normal")