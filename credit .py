is_goodcredit = False
house_price = 1_000_000

if is_goodcredit:
    down_payment = house_price * 0.10
else:
    down_payment = house_price * 0.20

print(f"The down payment is ${down_payment}")
