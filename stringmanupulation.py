s = "Hello World Python"

# 1. BASIC INFO
print(len(s))                    # 18 - length
print(type(s))                   # <class 'str'>

# 2. CASE CONVERSION
print(s.upper())                 # HELLO WORLD PYTHON
print(s.lower())                 # hello world python
print(s.capitalize())            # Hello world python
print(s.title())                 # Hello World Python
print(s.swapcase())              # hELLO wORLD pYTHON

# 3. SLICING
print(s[0])                      # H
print(s[-1])                     # n
print(s[0:5])                    # Hello
print(s[6:11])                   # World
print(s[::2])                    # HloWrdPto
print(s[::-1])                   # nohtyP dlroW olleH  (reverse)
print(s[0:10:2])                 # HloWr

# 4. SEARCH
print(s.find("World"))           # 6  (index where found, -1 if not)
print(s.index("World"))          # 6  (same but throws error if not found)
print(s.count("l"))              # 3
print(s.startswith("Hello"))     # True
print(s.endswith("Python"))      # True
print("World" in s)              # True
print("Java" not in s)           # True

# 5. REPLACE & REMOVE
print(s.replace("World", "AIUB"))        # Hello AIUB Python
print(s.replace("l", "L"))              # HeLLo WorLd Python
print("  hello  ".strip())              # hello  (removes both sides)
print("  hello  ".lstrip())             # hello   (removes left)
print("  hello  ".rstrip())             #   hello  (removes right)
print(s.removeprefix("Hello "))         # World Python
print(s.removesuffix(" Python"))        # Hello World

# 6. SPLIT & JOIN
print(s.split(" "))              # ['Hello', 'World', 'Python']
print(s.split("o"))              # ['Hell', ' W', 'rld Pyth', 'n']
words = ['Hello', 'World', 'Python']
print(" ".join(words))           # Hello World Python
print("-".join(words))           # Hello-World-Python
print("".join(words))            # HelloWorldPython

# 7. CHECK TYPE
print("hello".isalpha())         # True  (only letters)
print("hello123".isalpha())      # False
print("12345".isdigit())         # True  (only digits)
print("hello123".isalnum())      # True  (letters and digits)
print("   ".isspace())           # True  (only spaces)
print("Hello World".istitle())   # True
print("HELLO".isupper())         # True
print("hello".islower())         # True

# 8. FORMATTING
name = "Alif"
age = 21
print(f"Name: {name}, Age: {age}")                    # f-string
print("Name: {}, Age: {}".format(name, age))          # .format()
print("Name: %s, Age: %d" % (name, age))              # % operator
print(f"{3.14159:.2f}")                               # 3.14  (2 decimal places)
print(f"{name:>10}")                                  # right align in 10 chars
print(f"{name:<10}")                                  # left align in 10 chars
print(f"{name:^10}")                                  # center align in 10 chars

# 9. PADDING & FILL
print("42".zfill(5))             # 00042  (fill zeros on left)
print("hello".center(11, "-"))   # ---hello---
print("hello".ljust(10, "."))    # hello.....
print("hello".rjust(10, "."))    # .....hello

# 10. ENCODE / DECODE
print(s.encode("utf-8"))         # b'Hello World Python'

# 11. MISC
print(s * 2)                     # Hello World PythonHello World Python
print("Hello" + " " + "World")  # Hello World  (concatenation)
print(ord("A"))                  # 65  (ASCII value)
print(chr(65))                   # A   (char from ASCII)
print(list(s))                   # converts string to list of characters
print(tuple(s))                  # converts string to tuple of characters