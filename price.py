has_godcredit = True
house_price = 1000000
if has_godcredit:
    down_payment = house_price * 0.10
else:
    down_payment = house_price * 0.20
print(f"The down payment is ${down_payment}")