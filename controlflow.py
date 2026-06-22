marks = 0

# Note: In Python, 0 evaluates to False. 
# So this specific block will jump straight to the 'else' and print "Fail".
if marks:
    print("Pass")
elif marks >= 90:
    print("A+")
else:
    print("Fail")

is_raining = False
is_moroccan = False

if is_raining:
    print("Take an umbrella")
    if is_moroccan:
        print("Wear a djellaba")
else:
    print("Enjoy the sunshine")

x = int(input("Enter a number: "))
print(x + 1)

day = 3
match day:
    # case 1 | 2 | 3 | 4 | 5:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday") 
    case _:
        print("Invalid day")

x = 10
while x > 0:
    print(x)
    x -= 1

# Pera is in for loop

for i in range(5):
    print(i)

print(list(range(5)))

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

numbers = [0, 1, 2, 3, 4]
numbers = list(range(5))


for i in range(5):
    print(i, end=" ")
print()
for i in range(1, 6):
    print(i, end=" ")
print()
for i in range(2, 11, 2):
    print(i, end=" ")
for i in range(10, 0, -2):
    print(i, end=" ")
print()

word = "Python"
for char in word:
    print(char)

marks = [85, 92, 78, 96, 88]
print(sum(marks))
total = 0
for mark in marks:
    total += mark
print(total)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
    print("-----")

i = 0
while True:
    i += 1
    if i == 2:
        continue
    print(i)
    if i >= 5:
        break

n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)