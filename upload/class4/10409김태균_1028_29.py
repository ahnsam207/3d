import random
com = random.randint(1,3) #1:가위, 2:바위, 3:보
user =int(input("가위(1), 바위(2), 보(3) 입력:"))

if user ==1:
    if com == 1:
        print(f"com은 가위, user는 가위 비겼습니다.")
    elif com == 2:
        print(f"com은 바위, user는 가위 졌습니다.")
    else :
        print(f"com은 보, user는 가위 이겼습니다.")
if user == 2 :
    if com == 1:
        print(f"com은 가위, user는 바위 이겼습니다.")
    elif com == 2:
        print(f"com은 바위, user는 바위 비겼습니다.")
    else:
        print(f"com은 보, user는 바위 졌습니다.")
if user == 3:
    if com == 1:
        print(f"com은 가위, user는 보 졌습니다.")
    elif com == 2:
        print(f"com은 바위, user는 보 이겼습니다.")
    else :
        print(f"com은 보, user는 보 비겼습니다.")
