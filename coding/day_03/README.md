# Functions

- A function is a named block of code that does one job..
- A function lets you put logic in one place and reuse it whenever needed.
- In DevOps/SRE/Platform work, functions are used for things like:
  * checking service status
  * validating input
  * computing health status
  * reading files
  * parsing logs
  * calling APIs
  * formatting alerts
  * retrying commands
- Ex:
      ```python
      def greet():
          print("Hello")
      ```    
      To run it:
      
      ```python
      greet()
      ```
---

## Function with parameters

- A parameter is input to a function.
- Ex:
  ```python
  def greet(name):
      print(f"Hello {name}")
  ```
  Call it:
  
  ```python
  greet("DevOps")
  ```
---

## Function with return value

- A function can give back a result using `return`.
- Ex:
  ```python
  def square(num):
      return num * num
  ```
  Use it:
  
  ```python
  result = square(5)
  print(result)
  ```
