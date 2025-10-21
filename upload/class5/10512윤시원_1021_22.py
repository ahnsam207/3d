국어 = int(input("국어 성적"))
영어 = int(input("영어 성적"))
총점 = 국어 + 영어
평균 = round(총점/2,1)
if 평균>=90:
    print("A")
elif 평균>=80:
    print("B")
elif 평균>=70:
    print("C")
elif 평균>=60:
    print("D")
else :
    print("F")
