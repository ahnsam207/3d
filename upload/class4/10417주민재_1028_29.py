import random
c = random.randint(1,3)
u = int(input("가위(1),바위(2),보(3)를 입력:"))

if u==1:
    if c == 1:
        print("무승부")
    elif c == 2:
        print("패배")
    elif c == 3:
        print("승리")

if u==2:
    if c == 1:
        print("승리")
    elif c == 2:
        print("무승부")
    elif c == 3:
        print("패배")

if u==3:
    if c == 1:
        print("패배")
    elif c == 2:
        print("승리")
    elif c == 3:
        print("무승부")

