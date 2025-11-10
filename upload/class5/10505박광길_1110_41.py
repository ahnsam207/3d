이름=[]
while True:
    temp=input("이름입력(종료는 q입력):")
    if temp== 'q':
        break
    else:
        이름.append(temp)
print(f"이름:{str(이름)}")
