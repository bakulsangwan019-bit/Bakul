leap_year = int(input("Year : "))

if leap_year%4 == 0 :
    print("Its a Leap Year")
elif leap_year%100 != 0 :
    print("Not a leap year")
elif leap_year%400 != 0 :
     print("Its a Leap Year")
else:
    print("Not a leap year")