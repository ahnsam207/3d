import random
com=random.randint(1,2)
user=int(input("홀(1),짝(2)을 선택하세요:"))
if com==user:
    if user == 1:
        print("컴퓨터는 홀,당신은 홀 *성공*입니다.")
    else:
        print("컴퓨터는 짝,당신은 짝 *성공*입니다.")
else:
    if user == 1:
        print("컴퓨터는 짝,당신은 홀 *실패*입니다.")
    else:
        print("컴퓨터는 홀,당신은 짝 *실패*입니다.")
