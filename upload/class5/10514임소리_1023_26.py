temp = int(input('온도:'))

if temp>=25:
    print('반팔을 입으세요.')
elif 24>temp>=15:
    print('가벼운 겉옷을 입으세요.')
elif 15>temp:
    print('두꺼운 외투를 입으세요.')
