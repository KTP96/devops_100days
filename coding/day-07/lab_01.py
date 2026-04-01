"""
Invalid Integer
"""

try:
    value=int("abc")
    print(value)
except ValueError:
    print("Invalid Number")