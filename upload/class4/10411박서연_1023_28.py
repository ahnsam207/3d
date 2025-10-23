import random #랜덤 함수 툴 불러오기

입력 = int(input("홀(1),짝(2)을 선택하세요:"))
com = random.randint(1,2)

if(com ==1):
    com1 = '홀'
else:
    com1 = '짝'

if(입력 == 1):
    a = '홀'
else:
    a = '짝'

if(입력 == com):
    print(f"컴퓨터는 {com1},당신은 {a} *성공*입니다.")
else:
    print(f"컴퓨터는 {com1},당신은 {a} *실패*입니다.")
