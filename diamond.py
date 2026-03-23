height = 4
for i in range(height):
    for j in range(height -i - 1):
        print(" " , end="")
    for k in range(2*i + 1):
        print("*", end ="")
    print()
for i in range(3,0,-1):
    for j in range(4-i):
        print(" " , end="")
    for k in range(2*i - 1):
        print("*", end ="")
    print()