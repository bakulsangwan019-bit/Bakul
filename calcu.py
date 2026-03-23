x = float(input("Number1: "))
y = float(input("Number1: "))
z = input("Calculate: ")
if z == "sum":
    print(f"Sum of x and y is: {x+y}")
elif z == "subtraction":
    print(f"Subtraction of x nad y is : {x-y}")
elif z == "multiplication":
    print(f"Multiplication of x and y is : {x*y}")
elif z == "division" :
     print(f"Division of x and y is : {x/y}")
else:
    print("Invalid")