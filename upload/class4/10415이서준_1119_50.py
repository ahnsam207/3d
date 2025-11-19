import random as r

sr = ["가위", "바위", "보"]
ru = {0:1, 1:2, 2:0}
c = r.randrange(3)
u = int(input("가위(0), 바위(1) (2) 중 선택: "))
print(f"u ={sr[u]}, com = {sr[com]}")
if u == com:
    print('비김')
elif ru[com] == u:
    print('이김')
else:
    print('짐')
