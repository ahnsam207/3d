import random
선택=int(input("홀(1),짝(2)을 선택하세요:"))

com = random.randint(1,2)

if 선택==com:
    print(f"컴퓨터는 {com}, 당신은 {선택} *성공*입니다.")
else: print(f"컴퓨터는 {com}, 당신은 {선택} *실패*입니다.")
