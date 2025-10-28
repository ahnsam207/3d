import random
com = random.randint(1,3)
user =int(input("가위(1),바위(2),보(3):"))
if user == com:
          print("무승부")
elif user==1 and com==2:
    print("졌습니다")
elif user==2 and com==1:
    print("이겼습 니다")
elif user==3 and com==1:
    print("졌습니다")
elif user==1 and com==3:
    print("이겼습니다")
elif user==2 and com==3:
    print("졌습니다")
elif user==3 and com==2:
    print("이겼습니다")
else:
    print("입력을 다시확인해주세요")
