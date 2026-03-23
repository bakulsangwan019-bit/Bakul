count = 1

while count <= 5:
    num = count
    column = 1

    while column <= count:
        print(num, end="")
        num -= 1
        column += 1

    print()
    count += 1