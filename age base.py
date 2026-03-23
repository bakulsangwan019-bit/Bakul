x = int(input("Age: "))

if x < 13:
    print("Child")
elif x <= 17:
    print("Teen")
elif x <=59:
    print("Adult")
else:
    print("Senior")