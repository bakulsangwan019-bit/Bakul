balnce_amount = 10000
user = int(input("Withdrawal_amount: "))

if user <=0:
    print("Invalid Amount")
elif user > balnce_amount:
    print("Insufficient Balance")
else:
    print("Withdrwal Successful")