import random

user = int(input("홀(1), 짝(2)을 선택하세요: "))

com = random.randint(1, 2)

com_str = "홀" if com == 1 else "짝"
user_str = "홀" if user ==1 else "짝"

print(f"컴퓨터는 {com_str},  당신은 {user_str}")

if user== com:
    print("*성공*입니다.")
else:
    print("*실패*입니다.")
