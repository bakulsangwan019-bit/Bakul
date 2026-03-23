num1 = float(input("Number1 : "))
num2 = float(input("Number2 : "))
num3 = float(input("Number3 : "))

if num1>num2 and num1 > num3:
    print("The largest is num1")
elif num2>num1 and num2 > num3:
    print("The largest is num2")
else:
    print("The largest is num3")
