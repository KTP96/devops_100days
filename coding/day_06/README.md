# Day 6 — Files

## **Reading data from files**

* log files
* config files
* CSV/text reports
* deployment manifests
* inventory files
* monitoring outputs
* generated status reports

# Why files matter in DevOps

* read a server inventory file
* scan logs for errors
* read a config file
* process metrics from a text report
* generate alert summaries
* store automation output in a file
  
---

# Opening a file

```
with open("servers.txt", "r") as file:
    content = file.read()
    print(content)
```
* `open(...)` opens the file
* `"r"` means read mode
* `with` safely closes the file automatically
* `file.read()` reads all content

---

# Reading line by line

```
with open("servers.txt", "r") as file:
    for line in file:
        print(line)
```

Each line often ends with `\n`, so usually use `strip()`:

```
with open("servers.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

# Parsing file data

`servers.txt`

```
web-01,45,60
web-02,82,77
db-1,91,88
cache-1,67,72
```

Then,

```
with open("servers.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split(",")

        server = parts[0]
        cpu = int(parts[1])
        memory = int(parts[2])

        print(server, cpu, memory)
```
---

# Writing to a file

```
with open("report.txt", "w") as file:
    file.write("Server health report\n")
    file.write("web-01 --> NORMAL\n")
```

## Modes

* `"r"` → read
* `"w"` → write (overwrites file)
* `"a"` → append

---
