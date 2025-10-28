import random

com =  random.randint(1,3)

user = int(input("가위(1),바위(2),보(3) 입력:"))

if user == 1:
    if com == 1:
           print("당신은 가위, 컴도 가위 무승부입니다.")
           
    elif com == 2:
           print("당신은 가위, 컴은 바위 졌습니다.")

    else:
           print("당신은 가위, 컴은 보 이겼습니다.")

if user == 2:
    if com == 1:
           print("당신은 바위, 컴은 가위 이겼습니다.")
    elif com == 2:
           print("당신은 바위, 컴도 바위 무승부입니다.")
    else:
           print("당신은 바위, 컴은 보 졌습니다.")
if user == 3:
    if com == 1:
           print("당신은 보, 컴은 가위 졌습니다.")
    elif com == 2:
           print("당신은 보, 컴은 바위 이겼습니다.")
    else:
           print("당신은 보, 컴은 보 비겼습니다.")
