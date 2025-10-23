import random

com = random.randint(1,2)

a = int(input("홀(1),짝(2)을 선택하세요:"))

if(com == 1):
    com1 = '홀'
else:
    com1 = '짝'

if(a == 1):
    a1 = '홀'
else:
    a1 = '짝'
    
if(com == a):
    print(f"컴퓨터는 {com1},당신은 {a1} *성공*입니다.")
else:
    print(f"컴퓨터는 {com1},당신은 {a1} *실패*입니다.")
