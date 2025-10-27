import random
com = random. randint(1,2)
user = input("홀(1),짝(2)을 선택하세요")
if com ==user:
    if user=="1":
        print("computer홀 user홀 맞았어요")
    else:
        print("computer짝 user짝 맞았어요")
else:
    if user=="1":
        print("computer짝 user홀 틀렸어요")
    else:
        print("computer홀 user짝 틀렸어요")
    

