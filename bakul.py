weight = float(input('Weight : '))
unit = input("(L)bs or (K)g : ").upper()

if unit == "L":
    convertion = weight * 0.45
    print(f"You are {convertion} kilos")
elif unit == "K":
    convertion = weight * 0.45
    print(f"You are {convertion} lbs")
else:
    print("Invalid")



