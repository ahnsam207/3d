c = {}

c['빨강'] = 'Red'
c['주황'] = 'Orange'
c['노랑'] = 'Yellow'
c['초록'] = 'Green'
c['파랑'] = 'Blue'
c['남색'] = 'Indigo'
c['보라'] = 'Violet'
c['분홍'] = 'Pink'
c['흰색'] = 'White'
c['검정'] = 'Black'

while True:
    a = input('좋아하는 색을 입력하세요. 종료하려면 "끝"을 입력하세요.')

    if a == "끝":
        print('종료합니다')
        break
    elif a in c:
        print(f'{a} --> {c[a]}')
    else:
        print('그런 색은 없습니다.')
    print('='*30)
