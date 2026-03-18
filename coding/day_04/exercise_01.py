"""
Create a dictionary called instance with keys:
* id
* region
* status
Give it sample values and print all 3 individually.
"""

instance={
    "id":"i-123",
    "region":"us-west-2",
    "status":"RUNNING"
}

print(f"INSTANCE: {instance["id"]}")
print(f"REGION: {instance["region"]}")
print(f"STATUS: {instance["status"]}")

