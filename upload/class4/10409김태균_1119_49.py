# 빈 사전 생성
color = {}

color['빨강'] = 'Red'
color['파랑'] = 'Blue'
color['노랑'] = 'Yellow'
color['보라'] = 'Violet'
color['주황'] = 'Orange'
color['초록'] = 'Green'
color['남색'] = 'Indigo'
color['분홍'] = 'Pink'
color['검정'] = 'Black'

# 좋아하는 색 찾기
print(f'좋아하는 색을 입려하세요. 종료하려면 "끝"을 입력하세요.')

while True :
    favorite = input(f"당신이 좋아하는 색은 ?:")
    if favorite == "끝" :
        print(f"종료합니다.")
        break
    elif favorite in color :
        print(f'{favorite} --> {color[favorite]}')
    else :
        print(f" 그런 색이 없습니다.")
    print('==================================')
