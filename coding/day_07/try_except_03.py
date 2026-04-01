### Catching specific errors

try:
    num=int("abc")
except ValueError:
    print("Invalid Number")