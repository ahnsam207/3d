#빈 사전 생성
c = {}

c['빨강'] = 'Red'
c['파랑'] = 'Blue'
c['노랑'] = 'Yellow'
c['보라'] = 'Violet'
c['주황'] = 'Orange'
c['초록'] = 'green'
c['남색'] = 'Indigo'
c['분홍'] = 'Pink'
c['흰색'] = 'white'
c['검정'] = 'Black'

# 좋아하는 색 찾기
print('좋아하는 색을 입력하세요. 종료하려면 "끝"을 입력하세요.')

while True :
    favorite = input('당신이 좋아하는 색은?')
    if favorite == "끝" :
        print('종료합니다')
        break
    elif favorite in c :
        print(f'{favorite} --> {c[favorite]}')
    else :
        print('그런 색은 없습니다.')
    print("="*30)
