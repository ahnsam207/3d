
unpaid = int(input("미납금: "))
rate = float(input("할증률(%): "))


payment = int(unpaid + (unpaid * rate / 100))


print(f"최종 납부금액은 {payment}원입니다.")

