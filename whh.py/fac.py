result = 1
number = int(input("Number : "))

for Num in range(1, number+1):
    result = result * Num
    print("Num:", Num, "result:", result)


print(result)