color= {}
color['빨강']='RED';    color['파랑']='BLUE'
color['노랑']='YELLOW'; color['보라']='VIOLET'
color['주황']='ORANGE'; color['초록']='GREEN'
color['남색']='INDIGO'; color['분홍']='PINK'
color['흰색']='WHITE';  color['검정']='BLACK'

print('좋아하는 색을 입력하세요. 종료하려면 "끝"을 입력하세요.')

while True :
    favorite = input('당신이 좋아하는 색은?:')
    if favorite =="끝":
        print('종료합니다.')
        break
    elif favorite in color:
        print(f"{favorite} --> {color[favorite]}")
    else :
        print('그런 색이 없습니다.')
    print('-----------------------------------------')
    
