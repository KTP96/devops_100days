"""
Write a function called get_disk_status(disk):

CRITICAL if disk >= 90

WARNING if disk >= 75

NORMAL otherwise

Test it with 60, 78, 95.

"""

def get_disk_status(disk):
    if disk>=90:
        return "CRITICAL"
    elif disk>=75:
        return "WARNING"
    else:
        return "NORMAL"

test_data=[60,78,95]
for i in range(len(test_data)):
    status=get_disk_status(test_data[i])
    print(f"Status={status}")