import random
com = random.randint(1,3)
user = int(input("가위(1),바위(2),보(3) 입력:"))
if user == 1:
    if com == 1:
        print("컴퓨터:가위 유저:가위 비겼다!!")
    elif com == 2:
        print("컴퓨터:바위 유저:가위 졌다!!")
    else:
         print("컴퓨터:보 유저 가위 이겼다!!")
if user == 2:
    if com == 1:
        print("컴퓨터:가위 유저:바위 이겼다!!")
    elif com == 2:
        print("컴퓨터:바위 유저:바위 비겼다!!")
    else:
        print("컴퓨터:보 유저 주먹 졌다!!")
if user == 3:
    if com == 1:
        print("컴퓨터:가위 유저:보 졌다!!")
    elif com == 2:
        print("컴퓨터:바위 유저:보 이겼다!!")
    else:
        print("컴퓨터:보 유저:보 비겼다!!")
                
                
