import random

com = random.randint(1,3)

user = int(input("가위(1), 바위(2), 보(3)을 입력하세요:"))

if com == 1:
    print("컴퓨터는 가위를 냈습니다.")
elif com == 2:
    print("컴퓨터는 바위를 냈습니다.")
else:
    print("컴퓨터는 보를 냈습니다.")

if user == com:
    print("비겼습니다.")
elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
    print("이겼습니다.")
else:
    print("졌습니다.")
