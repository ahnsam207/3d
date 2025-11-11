이름 = []

while True:
    temp = input("이름 입력(종료는 q 입력):")

    if temp == 'q':
        break
    else:
        이름.append(temp)

print("이름:" + str(이름))
