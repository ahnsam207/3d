def c2f(temC) :
    tempF = tempC * 1.8 + 32
    print(f'{tempC:.2f}섭시온도는 {tempF:.2f}화씨입니다.')

cel = float(input('섭씨 온도를 입력하세요: '))
c2f(cel)
