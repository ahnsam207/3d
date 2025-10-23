import random

com = random.randint(1,2)

도연 = int(input("홀(1), 짝(2)을 선택하세요 :"))

if com == 도연 :
    print(f"컴퓨터는 {com},당신은 {도연} *성공*입니다.")

else:
    print(f"컴퓨터는 {com},당신은 {도연} *실패*입니다.")

