import random

user = int(input("홀(1), 짝(2)을 선택하세요:"))

com = random.randint(1,2)

if com == 1:
    print("컴퓨터는 홀입니다.")
else:
    print("컴퓨터는 짝입니다.")

if user == com:
    print("당신은", "홀" if user == 1 else "짝", "*성공*입니다.")
else:
    print("당신은", "홀" if user == 1 else "짝", "*실패*입니다.")
