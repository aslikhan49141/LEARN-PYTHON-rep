def res(a: str) -> int:
    position = 0
    for char in a:
        if char == "R":
            position += 1
        elif char == "L":
            position -= 1
    return position

x = input()
print(res(x))