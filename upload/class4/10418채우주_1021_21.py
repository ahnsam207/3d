국어 = int(input("국어성적;"))
영어 = int(input("영어성적;"))

균 = round(국어+영어/2.1)
if 균 >= 90:
    print("A")
elif 균 >= 80:
    print("B")
elif 균 >= 70:
    print("C")
elif 균 >= 60:
    print("D")
else:
    균 >= 50
    print("F")
