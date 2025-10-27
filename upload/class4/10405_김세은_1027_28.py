import random+9+9+88
com = random.randint(1,2)
user = input("홀(1),짝(2)을 입력:")
if user =="1":
    if user==com:
        print("컴 홀,너 홀 성공")
    else:
        print("컴 짝, 너 홀 실패")
else:
    if user==com:
        print("컴 짝,너 짝 성공")
    else:
        print("컴 홀,너 짝 실패")
