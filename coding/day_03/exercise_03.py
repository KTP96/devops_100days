"""
Write a function called is_high_cpu(cpu):

return True if cpu >= 80

else return False

Test it with 50 and 90.

"""
def is_high_cpu(cpu):
    if cpu>=80:
        return True
    else:
        return False


test_data=[50,90]
for i in range(len(test_data)):
    cpu_usage_status=is_high_cpu(test_data[i])
    print(f"High CPU Usage: {cpu_usage_status}" )