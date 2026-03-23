row = 5
for i in range(row):
    for s in range(row - i - 1):
        print(" " , end="")
    for st in range( 2*i + 1):
        print("*", end="")
    print()