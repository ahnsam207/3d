kor = int(input("kor:"))
eng = int(input("eng:"))

chd = (kor + eng)
vud = round(chd/2,1)

if vud >= 90:
    print("A")
elif vud >= 80:
    print("B")
elif vud >= 70:
    print("C")
elif vud >= 60:
    print("D")
else:
    print("F")
