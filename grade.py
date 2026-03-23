grade_system = int(input("Number : "))

if 90<=grade_system<=100:
    print("GradeA")
elif 80 <= grade_system < 90:
    print("GradeB")
elif 70<= grade_system < 80:
    print("GradeC")
elif 60<= grade_system < 70:
    print("GradeD")
else:
    print("Fail")