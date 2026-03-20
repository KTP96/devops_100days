# Day 5 — Strings and parsing

## **Strings, split(), strip(), lower(), and parsing monitoring/log text**

### `strip()`

- Removes extra spaces or newline characters.
- Example: 
  ```python
  line = "   nginx   "
  print(line.strip())
  ```
Output:
```python
nginx
```
---

### `lower()` and `upper()`
- Makes string lowercase or uppercase.
- 
```python
status = "RUNNING"
print(status.lower())
```
Output:
```python
running
```
Useful when input may come in different letter styles.

Example:

```python
status = input("Enter status: ").strip().lower()
if status == "running":
    print("Service is healthy")
```

---

### `split()`
- It splits text into pieces.
- Example:
- 
```python
line = "web-01,82,77"
parts = line.split(",")
print(parts)
```
Output:
```python
['web-01', '82', '77']
```

```python
name = parts[0]
cpu = parts[1]
memory = parts[2]
```
---

# Converting parsed values

- After `split()`, values are strings.

```python
cpu = int(parts[1])
```
---

# Checking substrings

- 
```python
line = "ERROR: nginx failed to start"

if "ERROR" in line:
    print("Error found")
```
---
