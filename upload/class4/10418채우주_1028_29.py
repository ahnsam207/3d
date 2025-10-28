import random
com = random.randint(1,3)
user = int(input("가위 (1) 바위 (2) 보 (3) 중에 숫자를 고르세요!;"))
if user == 1:
           if com ==1:
               print("비겼습니다...")
           elif com == 2:
               print("아쉽지만 실패...")
           else:
               print("마침내 승리를 따갑니다!!")
elif user == 2:
           if com ==2:
               print("비겼습니다...")
           elif com == 3:
               print("아쉽지만 실패...")
           else:
               print("마침내 승리를 따갑니다!!")
elif user == 3:
           if com ==3:
               print("비겼습니다...")
           elif com == 1:
               print("아쉽지만 실패...")
           else:
               print("마침내 승리를 따갑니다!!")
    

