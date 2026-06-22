x = int(input("Enter a number: "))

match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case 6:
        print("six")
    case 7:
        print("seven")
    case 8:
        print("eight")
    case 9:
        print("nine")    
    case _:
        print(f"You entered {x}, which is not between 1 and 9.")