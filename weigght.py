weight = int(input(" Weight : "))
unit = input("(L)bs or (K)g : ")

if unit.upper() == "L":
    convertion = weight * 0.45
    print(f"You are {convertion} kgs")
else:
    convertion = weight/.45
    print(f"You are {convertion} lbs")