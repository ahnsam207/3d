import random
com  = random.randint(1,3)
user = int(input("가위(1)바위(2)보자기(3)을 입력:"))

if user == "1": 
   if user == com:
       print("컴퓨터 보자기,사용자 가위 성공")
   elif:
       print("컴퓨터 주먹,사용자 가위 실패")
   else:
       print("컴퓨터 가위,사용자 가위 실패")

if user == "2": 
   if user == com:
       print("컴퓨터 가위,사용자 바위 성공")
    elif:
       print("컴퓨터 보자기,사용자 바위 실패")
    else:
       print("컴퓨터 바위,사용자 바위 실패")


if user == "3": 
   if user == com:
       print("컴퓨터 주먹,사용자 보자기 성공")
   elif:
       print("컴퓨터 가위,사용자 보자기 실패")
   else:
       print("컴퓨터 보자기,사용자 보자기 실패")



