color = {}

color['빨강'] = 'Red', color['파랑'] = 'Blue'
color['노랑'] = 'Yellow', color['보라'] = 'Violet'
color['주황'] = 'Orange', color['초록'] = 'Green'
color['남색'] = 'Indigo', color['분홍'] = 'Pink'
color['흰색']= 'White', color['검정'] = 'Black'

while Ture:
    favorite = input('당신이 좋아하는 색은 ? : ')
    If favorite == "끝":
        print('종료합니다.')
        break
    elif favorite in color :
        print(f'{favorite} --> {color[favorite]}')
    else :
        print('그런 색이 없습니다')
    
