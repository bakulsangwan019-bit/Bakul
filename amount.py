balnce_amount = 10000
user = int(input("Withdrawal_amount: "))
if user > balnce_amount:
    print("Insufficient Balance")
elif user <=0:
    print("Invalid Amount")
else:
    print("Withdrwal Successful")