# Day 7 — Error handling with `try/except`

## Writing safer Python scripts

In DevOps/SRE/platform work, scripts often fail because of things like:

* bad input
* missing files
* invalid numbers
* malformed data
* unexpected API output
* missing keys
* command failures

---

## 1. What is `try/except`?

It lets Python try something risky, and if it fails, handle the error gracefully.

Example:

```python
try:
    value = int("abc")
except:
    print("Invalid number")
```

Without `try/except`, the script crashes.

---

## 2. Why this matters in DevOps

Imagine parsing a file like:

```text
web-01,45,60
web-02,abc,77
db-1,91,88
```

If you do:

```python
cpu = int(parts[1])
```

on `"abc"`, your script crashes.

With `try/except`, you can skip the bad line and continue.

---

## 3. Basic syntax

```python
try:
    risky_code_here
except:
    print("Something went wrong")
```

---

## 4. Better style: catch specific errors

Example:

```python
try:
    value = int("abc")
except ValueError:
    print("Not a valid integer")
```

This is better than plain `except:`.

Common ones you’ll use:

* `ValueError`
* `FileNotFoundError`
* `IndexError`
* `KeyError`

---

## 5. Example with file parsing

```python
line = "web-02,abc,77"
parts = line.split(",")

try:
    cpu = int(parts[1])
    memory = int(parts[2])
    print(cpu, memory)
except ValueError:
    print("Bad numeric data in line")
```

---

## 6. Example with missing file

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")
```
