## Function for status classification

def get_cpu_status(cpu):
    if cpu>=90:
        return "CRITICAL"
    elif cpu>=75:
        return "WARNING"
    else:
        return "NORMAL"

print(get_cpu_status(100))
print(get_cpu_status(90))
print(get_cpu_status(75))
print(get_cpu_status(80))
print(get_cpu_status(65))