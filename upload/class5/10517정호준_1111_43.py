name = []

while True:

    temp = input("이름 입력(종료는 q 입력):")

    if temp == 'q' or temp == 'quit':
        break
    else:
        name.append(temp)
        #quit
    I_name = input("찾을 학생 이름 입력:")
    print('' .join(name))
    for i, I_name in enumerate(name):
        if I_name == name:
            print(f'학생은 {i+1}번 입니다')
            break
        else:
            if i == len(name) -1:
                print("학생이 없습니다")
