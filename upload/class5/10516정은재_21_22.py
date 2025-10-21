k = int(input("국어 성적 입력 : "))
e = int(input("영어 성적 입력 :"))

pr = (k + e / 2)


if pr >= 90:
    print("A")
elif pr >= 80:
    print("B")
elif pr >= 70:
    print("C")
elif pr >= 60:
    print("D")
else:
    print("F")
