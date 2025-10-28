import random
c = random.randint(1,3)
u = int(input("가위(1), 바위(2), 보(3) 입력:nn b"))
if u==1:
    if c==1:
        print("컴퓨터는 가위, 당신은 가위 비겼습니다.")
    elif c==2:
        print("컴퓨터는 바위, 당신은 가위 졌습니다.")
    elif c==3:
        print("컴퓨터는 보, 당신은 가위 이겼습니다.")
if u==2:
    if c==1:
        print("컴퓨터는 가위, 당신은 바위 이겼습니다.")
    elif c==2:
        print("컴퓨터는 바위, 당신은 바위 비겼습니다.")
    elif c==3:
        print("컴퓨터는 보, 당신은 바위 졌습니다.")
if u==3:
    if c==1:
        print("컴퓨터는 가위, 당신은 보 졌습니다.")
    elif c==2:
        print("컴퓨터는 바위, 당신은 보 이겼습니다.")
    elif c==3:
        print("컴퓨터는 보, 당신은 보 비겼습니다.")
