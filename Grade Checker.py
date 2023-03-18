
while True:
    # student_name = input("Enter your name: ")
    student_score = float(input("Enter your score out of 100:  "))

    if student_score < 0 or student_score > 100:
        print("Out of score range")
    elif student_score >= 75 or student_score == 100:
        print("GRADE A1")
    elif student_score >= 70 or student_score == 74:
        print("GRADE B1")
    elif student_score >= 65 or student_score == 69:
        print("GRADE B3")
    elif student_score >= 60 or student_score == 64:
        print("GRADE C4")
    elif student_score >= 55 or student_score == 59:
        print("GRADE C5")
    elif student_score >= 50 or student_score == 54:
        print("GRADE C6")
    elif student_score >= 45 or student_score == 49:
        print("GRADE D7")
    elif student_score >= 40 or student_score == 44:
        print("GRADE E8")
    elif student_score <= 39 or student_score == 0:
        print("GRADE F9")
