국어=int(input("성적입력"))
영어=int(input("성적입력"))
총점=국어+영어
평균=roud(총점/2,1)
print("평균"+str(평균))
if 평균>=90:
    print("우수상")
