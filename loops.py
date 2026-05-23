print("Range Loop")
for i in range(5):
    print(i)

print("List Loop")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("Index Loop")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

print("Dictionary Loop")
scores = {"Alif": 95, "Sneha": 98}
for name in scores:
    print(name, scores[name])

print("While Loop ")
count = 0
while count < 3:
    print(count)
    count = count + 1

print(" Break and Continue ")
for number in range(1, 10):
    if number == 3:
        continue
    if number == 6:
        break
    print(number)