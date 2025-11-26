def c2f(c):
    f = c * 1.8 + 32
    print(f"{c:.2f}섭씨온도는 {f:.2f}화씨입니다.")
cf = float(input("섭씨온도를 입력하시오. : "))
c2f(cf)
