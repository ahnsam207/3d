name = []
while True:
    temp = input("이름 입력(종료는 q 입력):")
    if temp =='q':
        break
    else:
        name.append(temp)
name = input("찾을 학생 이름 입력:")

for i, l_name in enumerate(name):
    if l_name == name:
        print("학생은"+str(i+1)+"번입니다.")
        break
    else:
        if i == len(name) - 1:
            print("학생이 없습니다.")
