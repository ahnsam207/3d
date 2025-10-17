국어=int(input("국어 성적을 입력하시오"))
영어=int(input("영어 성적을 입력하시오"))

평균=round((국어+영어)/2,1)

if 평균>=90:
    print("우수상")
else:
    print("노력상")
