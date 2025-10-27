import random
com = random.randint(1,2)
숫자 = int(input("홀 (1), 짝 (2)을 선택하세요:"))
if 숫자 ==com:
    print(f"컴퓨터는{com},당신은{숫자} *성공*입니다.")
else:
    print(f"컴퓨터는{com},당신은{숫자} *실패*입니다.")
