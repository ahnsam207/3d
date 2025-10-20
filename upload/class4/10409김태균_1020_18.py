국어 = int(input("국어 성적 입력:"))
영어 = int(input("영어 성적 입려:"))
총점 = 국어+영어
평균 = round(총점/2,1)
if 평균>=90:
    print("우수상")
else :
    print("노력상")
