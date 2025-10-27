import random
com=random.randint(1,100)

선택=int(input("홀(1) 짝(100)를 선택하세요:"))

if com==선택:
    print("컴퓨터는 {com}. 당신은 {선택} *성공*입니다.")
else:
    print("컴퓨터는 {com}. 당신은 {선택} *실패*입니다.")
