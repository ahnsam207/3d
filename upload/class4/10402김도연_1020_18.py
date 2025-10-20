kor = int(input("korean score:"))
eng = int(input("english score:"))

sum_total = kor + eng
result = round(sum_total/2,1)

if(result >= 90):
    print("우수상")
else:
    print("노력상")
