import random
com = random.randint(1,3)
user = int(input("가위(1), 바위(2), 보(3), 입력:"))
if user == 1:
    if com == 1:
        print('컴퓨터는 가위 당신은 가위 결과: 비김')
    elif com == 2:
        print('컴퓨터는 바위 당신은 가위 결과: 패배')
    else:
        print('컴퓨터는 보 당신은 가위 결과: 승리')
elif user == 2:
    if com == 1:
        print('컴퓨터는 가위 당신은 바위 결과: 승리')
    elif com == 2:
        print('컴퓨터는 바위 당신은 바위 결과: 비김')
    else:
        print('컴퓨터는 보 당신은 바위 결과: 패배')
elif user == 3:
    if com == 1:
        print('컴퓨터는 가위 당신은 보 결과: 패배')
    elif com == 2:
        print('컴퓨터는 바위 당신은 보 결과: 승리')
    elif com == 3:
        print('컴퓨터는 보 당신은 보 결과: 비김')

