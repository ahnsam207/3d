c = 0
s = 0

a = input("반복 횟수: ")
while not a.isdigit():
    a = input("반복 횟수: ")
a = int(a)
for i in range(a):
    v = int(input("값 입력: "))
    c = c + 1
    s = s + v
    print(f"v:{v}, c:{c}, s:{s}")
