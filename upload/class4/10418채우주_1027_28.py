import random
user = input("숫자를 입력 하세요! 홀(1) 짝(2) 를 입력!;")

com = random.randint(1,2)
if user == "1" and user == com:
        print("컴 홀 그리고 유저 홀 성공!")
else:
    print("컴 짝 그리고 유저 홀 실패!")
    
if user == "2" and user == com:
    print("컴 짝 그리고 유저 짝 성공!")
else:
    print("컴 홀 그리고 유저 짝 실패!")


    




 
