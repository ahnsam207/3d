import random

com = random.randint(1,3)

player = int(input("가위(1),바위(2),보(3) 중 선택해주세요:"))

result = ""

if(player == 1):
    p1 = "가위"
elif(player == 2):
    p1 = "바위"
elif(player == 3):
    p1 = "보"
else:
    print("잘못된 입력입니다.")

if(com == 1):
    com1 = "가위"
elif(com == 2):
    com1 = "바위"
elif(com == 3):
    com1 = "보"
else:
    print("잘못된 입력입니다.")


if(player == com):
    result = '무승부' 
elif(player == 2 and com == 1):
    result = '승리'
elif(player == 3 and com == 1):
    result = '패배'
elif(player == 1 and com == 2):
    result = '패배'
elif(player == 1 and com == 3):
    result = '승리'
elif(player == 2 and com == 3):
    result = '패배'
else:
    print("error")


print(f"당신은 '{p1}' 이고 com은 '{com1}' 입니다. 당신은 {result}했습니다.")
    

