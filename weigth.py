weight_kg = input("Enter weigth in kg: ")
_lbs = float(weight_kg) / 0.45
lbs = input("Enter weight in lbs: ")
kg = float(lbs) * 0.45
kg = True
_lbs = True

if _lbs or kg:
    print(f"In kg : {kg} and In lbs : {_lbs} ")
    