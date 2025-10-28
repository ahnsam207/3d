import random


com = random.randint(1,3)

user = int(input("가위(1), 바위(2), 보(3)"))

avg = com == user


if avg:
    print(" 비겼습니다")
if com == 1 and user == 1:
    print("컴퓨터는 보, 당신은 가위 이겼습니다")
elif com == 2 and user == 1:
    print("컴퓨터는 바위, 당신은 가위 졌습니다")
if com == 2 and user == 3:
    print("컴퓨터는 바위, 당신은 보 이겼습니다")
if com == 3 and user == 2:
    print("컴퓨터는 보, 당신은 바위 졌습니다")
elif com == 1 and user == 3:
    print("컴퓨터는 가위, 당신은 보 졌습니다")
    

