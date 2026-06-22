days=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
for d in days :
    print(d)


for i in range(40,20,-3) :
    print(i)



#while True:
    x = int(input("Enter a number: "))
    if x == 0:
        break
    elif x < 0:
        print("You entered a negative number. Please enter a positive number.")
        continue
    else:
        print(f"You entered {x}.")