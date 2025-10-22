온도 = int(input("온도를 입력하세요:"))

if 온도>=25 :
    print(f"반팔을 입으세요.")
elif (온도 >=15) and (온도<=24) :
    print(f"가벼운 겉옷을 입세요.")
else :
    print(f"두꺼운 외투를 입으세요.")
