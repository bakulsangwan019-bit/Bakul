while True:
    x = input("Enter a number: ")
    if x.isdigit():
        x = int(x)
        break
    else:
        print("Invalid input, try again")

print("You entered:", x)