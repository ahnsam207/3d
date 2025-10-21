국어=int(input("국어:"))
영어=int(input("영어:"))
합계=국어+영어
평균=round(합계/2,1)

if 평균>=90:
    print("A")
    
elif 평균>=80:
    print("B")

elif 평균>=70:
    print("C")

elif 평균>=60:
    print("D")

elif 평균>=50:
    print("E")

else:
    print("F")
