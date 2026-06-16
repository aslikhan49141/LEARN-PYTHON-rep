for x in range(10):
    print(x)

print("Another loop")

for y in range(5, 15):
    print(y)

print("Another loop")
for i in range(50 , 30 , -5) :
    print (f"i = {i}")

print("Another loop")
acc= 0
for j in range(1, 11):
    print(f"{acc}+{j}=  ", end="")
    acc += j
    print(acc)

print (f"Final value of acc = {acc}")