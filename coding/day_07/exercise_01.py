"""
Write a script that tries to convert "123" to int and prints it.
Then try "abc" and handle the error.

"""

try:
    number=int("abc")
    print(number)

except ValueError:
    print("Invalid Number")
