n = 5

for i in range(1, n+1):

    # print left spaces
    for s in range(n-i):
        print(" ", end="")

    # print pyramid area
    for j in range(2*i-1):

        if j == 0 or j == 2*i-2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()