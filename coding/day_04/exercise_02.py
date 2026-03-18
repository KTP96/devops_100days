"""
Create a dictionary called service with keys:
* name
* port
* running
Print: Service nginx is running on port 80
Use f-string.

"""

service={
    "name":"nginx",
    "port":80,
    "status":"running"
}

print(f"Service {service["name"]} is {service["status"]} on port {service["port"]}")

