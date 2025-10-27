import random
com = random.randint(1,2)
user = int(input("홀(1),짝(2)를 입력:"))

if user == 1:
    if user == com:
        print(f"com 홀, user 홀 성공")
    else :
        print(f"com 짝. user 홀 실패")
if user == 2:
    if user == com:
        print(f"com 짝, user 짝 성공")
    else :
        print(f"com 홀, user 짝 실패")
