import random
com = random.randint(1,3)
user = int(input("가위(1) 바위(2) 보(3)을 입력:"))

if user == 1:
    if com == 1:
        print("컴퓨터 보자기 사용자 가위, 승리")
    elif com == 2:
        print("컴퓨터 주먹 사용자 가위, 패배")
    else:
        print("컴퓨터 가위 사용자 가위, 무승부")

if user == 2:
    if com == 1:
        print("컴퓨터 가위 사용자 주먹, 승리")
    elif com == 2:
        print("컴퓨터 주먹 사용자 주먹, 무승부")
    else:
        print("컴퓨터 보자기 사용자 주먹, 패배")

if user == 3:
    if com == 1:
        print("컴퓨터 주먹 사용자 보자기, 승리")
    elif com == 2:
        print("컴퓨터 보자기 사용자 보자기 무승부")
    else:
        print("컴퓨터 가위 사용자 보자기, 패배")
