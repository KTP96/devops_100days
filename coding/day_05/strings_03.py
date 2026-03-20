### Strings basics

status=input("Enter status: ").strip().lower()
if status=="running":
    print("Service is healthy")
else:
    print("Service is not healthy")
