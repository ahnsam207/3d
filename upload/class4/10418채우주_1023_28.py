숫자 = int(input("홀(1), 짝(2)을 선택하세요;"))
import random
com = random.randint(1,2)
if 숫자 == com:
    print(f"컴퓨터는{com},당신은{숫자}성공입니다.")
else:
    print(f"컴퓨터는{com},당신은{숫자}실패입니다.")
    
