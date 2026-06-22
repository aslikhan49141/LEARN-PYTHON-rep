print("Hello", end=" ")
print("World!")


# Immutable datatypes: 
# Numeric: int, float, complex
# Sequence: str, tuple, range

# Mutable datatypes:
# Sequence: list
# Set: set
# Collection: dict

a = 10
print(id(a))
a = a + 2
print(id(a))
print(a)


a = [1, 2, 3]
a.append(4)
print(a)

x = 10
y = x
print(x)
print(y)
x = 20
print(x)
print(y)



a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a)
print(b)
a.append(4)
print(a)
print(b)
print(id(a))
print(id(b))

a = [1, 2, 9, 8, 3]
b = a.copy()
print(a)
print(b)
print(id(a))
print(id(b))

tuple_a = (1, 2, [3, 4],6)
print(tuple_a)
tuple_a[2].append(5)
print(tuple_a)
print(tuple_a[2][1])