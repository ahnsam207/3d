kor = int(input("국어 성적 입력:"))
eng = int(input("영어 성적 입력:"))


# porx = (kor + eng / 2)
porx = kor + eng
porx2 = round(porx/2,1)

if porx2>=90:
    print("국어" + str(kor) + "점")
    print("영어" + str(eng) + "점")
    print("평균 :" + str(porx2) + "점, 우수상")





