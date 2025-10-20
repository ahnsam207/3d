kor = int(input("국어:"))
eng = int(input("영어:"))
총점 = (kor + eng)
평균 = round(총점/2,1)
if 평균>=90:
    print("우수상")
else:
    print("노력상")
