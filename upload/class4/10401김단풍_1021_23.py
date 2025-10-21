kor = int(input("kor:"))
eng = int(input("eng:"))

chd = kor + eng
vud = round(chd/2.1)

if (kor >= 90) and (eng >= 90):
    print("수상내역:우수상")
elif vud >= 90:
    print("수상내역:장려상")
else:
    print("수상내역:노력상")
