import random
com = random.randint(1,3)
user =int(input("가위(1),바위,(2),보(3)를 선택하세요."))

if user==1 and com==1:
    print("컴퓨터는 가위, 당신은 가위 비겼습니다.")
elif user==1 and com==2:
    print("컴퓨터는 바위, 당신은 가위 졌습니다.")
elif user==1 and com==3:
    print("컴퓨터는 보, 당신은 가위 이겼습니다.")
elif user==2 and com==1:
    print("컴퓨터는 가위, 당신은 바위 이겼습니다.")
elif user==2 and com==2:
    print("컴퓨터는 바위, 당신은 바위 비겼습니다.")
elif user==2 and com==3:
    print("컴퓨터는 보, 당신은 바위 졌습니다.")
elif user==3 and com==1:
    print("컴퓨터는 가위, 당신은 보 졌습니다.")
elif user==3 and com==2:
    print("컴퓨터는 바위, 당신은 보 이겼습니다.")
elif user==3 and com==3:
    print("컴퓨터는 보, 당신은 보 비겼습니다.")
else:
    print("잘못입력 하셨습니다.")
