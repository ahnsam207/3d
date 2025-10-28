import random
com = random.randint(1,3)
user = int(input("가위(1),바위(2),보(3)를 선택하세요: "))

if user==1:
    if com ==1:
        print("컴퓨터는 가위, 당신은 가위 비겼습니다.")
    elif com ==2:
        print("컴퓨터는 바위, 당신은 가위 졌습니다.")
    elif com ==3:
        print("컴퓨터는 보, 당신은 가위 졌습니다.")
if user==2:
    if com ==1:
        print("컴퓨터는 가위, 당신은 바위 이겼습니다.")
    elif com ==2:
        print("컴퓨터는 바위, 당신은 바위 비겼습니다.")
    elif com ==3:
        print("컴퓨터는 보, 당신은 바위 졌습니다.")
if user==3:
    if com ==1:
        print("컴퓨터는 가위, 당신은 보 졌습니다.")
    elif com ==2:
        print("컴퓨터는 바위, 당신은 보 이겼습니다.")
    elif com ==3:
        print("컴퓨터는 보, 당신은 보 비겼습니다.")
if user==4:
    if com ==1:
        print("컴퓨터는 가위, 당신은 보 졌습니다.")
    elif com ==2:
        print("컴퓨터는 바위, 당신은 보 이겼습니다.")
    elif com ==3:
        print("컴퓨터는 보, 당신은 가위 이겼습니다.")        
