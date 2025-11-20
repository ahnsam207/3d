# 빈 사전 생성
color = {}

color ['빨강'] = 'red' ; color ['파랑'] = 'blue'
color ['노랑'] = 'Yellow' ; color ['보라'] = 'Violet'
color ['주황'] ='Orange' ; color ['초록'] = 'Green'
color ['남색'] = 'Indigo' ; color ['분홍'] = 'pink'
color ['흰색'] = 'White' ; color ['검정'] = 'Black'

# 좋아하는 색 찾기
print('좋아하는 색을 입력하셍. 종료하려면 "끝"을 입력하세요.')

while True :
    favorite = input('당신이 좋아하는 색은 ? : ')
    if favorite == "끝" :
        print('종료합니다.')
        break
    elif favorte in color :
        print(f'{favorite} --> {color[favorite]}')
    else :
        print('그런 색이 없습니다.')
    print("=" *30)
