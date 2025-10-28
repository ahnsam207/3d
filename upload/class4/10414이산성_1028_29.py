import random
com = random.randint(1,3)
user = int(input("가위(1),바위(2),보(3) 입력:"))

if user == 1:
    if com == 1:
        print("컴퓨터는 가위, 너도 가위. 비겼습니다.")
    elif com == 2:
        print("컴퓨터는 바위, 너는 가위. 졌습니다.")
    else :
        print("컴퓨터는 보, 너는 가위. 이겼습니다.")
if user == 2:
    if com == 1:
        print("컴퓨터는 가위, 너는 바위. 이겼습니다.")
    elif com == 2:
        print("컴퓨터는 보, 너도 보. 비겼습니다.")
    else :
        print("컴퓨터는 바위, 너는 가위. 졌습니다.")
if user == 3:
    if com == 1:
        print("컴퓨터는 가위, 너는 보. 졌습니다.")
    elif com == 2:
        print("컴퓨터는 보, 너도 가위. 이겼습니다.")
    else :
        print("컴퓨터는 바위, 너도 바위. 비겼습니다.")
