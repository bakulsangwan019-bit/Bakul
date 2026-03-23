PhoneNo = input("Number: ")
phnno = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
for c in PhoneNo:
    if c not in phnno:
        continue
    print(f"{phnno[c]}", end=" ")     