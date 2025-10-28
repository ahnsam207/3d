import random
com=random.randint(1,3)
user=int(input("가위(1),바위(2),보(3)를 선택하세요:"))
if user==com:
    print("비겼습니다.")
elif (user==1 and com==2 or 3):
        if com==2:
            print("졌습니다.")
        else:
            print("이겼습니다.")
elif (user==2 and com==1 or 3):
        if com==1:
            print("이겼습니다.")
        else:
            print("졌습니다.")
elif (user==3 and com==1 or 2):
        if com==1:
            print("이겼습니다.")
        else:
            print("졌습니다.")
else:
    print("입력을 다시 확인해주세요.")
