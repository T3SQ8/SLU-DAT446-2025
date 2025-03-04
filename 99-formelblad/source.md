---
geometry: margin=1in
classoption:
- twocolumn
title: Cheat Sheet SLU 2025
---

\pagenumbering{gobble}

# Data Structures

```python
# Lists
fruits = ["apple", "banana", "orange"]
fruits[1] == "banana"

# Dictionaries
fruit_weights = {
    "apple": 182,
    "banana": 118,
    "orange": 131,
}
fruit_weights["banana"] == 118
```

# Loops

```python
# For loop
for i in range(5):
    print(i)

# While loop
x = 0
while x < 5:
    print(x)
    x += 1
```

\newpage

# Functions

```python
def greet(name):
    return f"Hello, {name}!"

greet("Alice") == "Hello, Alice!"
```

# File handling

```python
# write to file
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# read from file
with open("file.txt", "r") as file:
    content = file.read()
```

# Objects & Classes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Bob", 25)
p.greet()
```
