국어 = int(input("국어 성적 입력:"))
영어 = int(input("영어 성적 입력:"))
총점 = 국어 + 영어
평균 = round(총점 / 2 , 1)
if(국어>=90)and(영어>=90):
    print("수상내역:우수상")
elif 평균>=90:
    print("수상내역:장려상")
else :
    print("수상내역:노력상")
