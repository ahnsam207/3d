국어 = int(input("국어:"))

영어 = int(input("영어:"))

성적 = int((국어+영어)/2)

if 성적>=90:
    print("A")
elif 성적>=80:
    print("B")
elif 성적>=70:
    print("C")
elif 성적>=60:
    print("D")
else:
    print("F")
    
