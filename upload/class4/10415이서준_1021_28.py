홀짝 = int(input('홀(1), 짝(2)을 선택하세요:'))
import random
com = random.randint(1,2)
if(com == 1):
    com = ('홀')
else:
    com = ('짝')
if(홀짝 == 1):
    홀짝 = ('홀')
else:
    홀짝 = ('짝')
if(홀짝 == com):
    print(f'컴퓨터는 {com}, 당신은 {홀짝} *성공*입니다.')
else:
    print(f'컴퓨터는 {com}, 당신은 {홀짝} *실패*입니다.')
