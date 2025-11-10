name = []


while True:
    temp = input("이름 입력(종료는  q 입력:")

    if temp =='q' or temp == 'quit':
        break
    
    else:
        name.append(temp)
print('이름 : \n')
print(' '.join(name))
