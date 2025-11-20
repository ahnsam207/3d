color = {}
color['빨강'] = 'red'
color['파랑'] = 'blue'
color['노랑'] = 'yellow'
color['보라'] = 'violet'
color['주황'] = 'orange'
color['초록'] = 'green'
color['남색'] = 'indigo'
color['분홍'] = 'pink'
color['흰색'] = 'white'
color['검정'] = 'black'

for i in color:
    print('%s는 %s입니다.' %(i, color[i]))

print('좋아하는 색을 입력하세요. 종료하려면 "끝"을 입력하세요.')

while True:
    favorite = input('당신이 좋아하는 색은?: ')
    if favorite == "끝":
        print('종료합니다.')
        break
    elif favorite in color:
        print(f'{favorite} --> {color[favorite]}')
    else:
        print('그런 색이 없습니다.')
print('='*30)
