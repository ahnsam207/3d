국어점수 = int(input("국어:"))
영어점수 = int(input("영어:"))
총점 = 국어점수+영어점수
평균 = 총점/2
if 평균>=90:
    print("우수상")
else:
    print("노력상")
