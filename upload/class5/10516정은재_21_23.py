k = int(input("국어 성적 입력 : "))
e = int(input("영어 성적 입력 :"))

sc = k + e
pr = round(sc/2,1)

if (k >= 90) and (e >=90):
    print("수상내역 : 우수상")
elif pr >=90:
    print("수상내역 : 장려상")
else:
    print("수상내역 : 노력상")


