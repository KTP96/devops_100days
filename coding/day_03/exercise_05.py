"""
Write a function called format_alert(server, status) that returns:

ALERT: web-1 is in CRITICAL state

Test it with:

("web-1", "CRITICAL")

("db-1", "WARNING")

"""

def format_alert(server,status):
    return f"ALERT: {server} is in {status} state"

message = format_alert("web-01","CRITICAL")
print(message)
message = format_alert("db-1", "WARNING")
print(message)