c = {}

c["빨"] = "r"; c["파"] = "b";c["노"] = "y";c["보"] = "v";c["주"] = "o";c["초"] = "g";c["남"] = "i";c["분"] = "p";c["흰"] = "w";c["검"] = "bk"

while True:
    f = input("당신이 좋아하는 색은 ? : ")
    if f == 'end':
        break
    elif f in c:
        print(f"{f} --> {c[f]}")
    else:
        print("색이 없습니다.")
    print("=" * 90 )
    print(" " * 90 )
    print(" " * 90 )
