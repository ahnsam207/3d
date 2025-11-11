이름 = []
while True:
    temp = input("이름 입력(종료는 q입력): ")
    if temp == "q":
        break
    else:
        이름.append(temp)
name = input("찾을 학생 이름 입력: ")
for i,ㅣ_name in enumerate(이름):
    if ㅣ_name==name:
        print("학생은 " +str(i+1) + "번입니다.")
        break
    else:
        if i == len(이름)-1:
            print("학생이 없습니다.")
    
