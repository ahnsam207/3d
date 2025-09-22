x = int(input("미납금:"))
y = int(input("할증률(%):"))

z = y/100

print("최종 납부금액은 "+str(int(x+x*z))+"원입니다.")
