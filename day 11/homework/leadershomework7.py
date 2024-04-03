exam_score = int(input("enter your exam's score here: "))

if exam_score > 90 and exam_score <= 100:
    print("A")
elif exam_score > 80 and exam_score <= 89:
    print("B")
elif exam_score > 70 and exam_score <= 79:
    print("C")
elif exam_score > 60 and exam_score <= 69:
    print("D")
elif exam_score < 60:
    print("F")