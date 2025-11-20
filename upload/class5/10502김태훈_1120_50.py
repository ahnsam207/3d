import random as r

sr = ['가위', '바위', '보']
rile = {0:1, 1:2 ,2:0}

com = r.randrange(3)
user = int(input("가위(0), 바위(1), 보(2) 중 선택: "))
print(f'user = {sr[user]}, com = {sr[com]}')

if user == com :
    prinr('비겼습니디')
elif rile[com] == user :
    print('당신이 이겼습니다')
else :
    print('컴퓨터가 이겼습니다')
