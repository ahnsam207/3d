def sum2n(n):
    total = 0
    for k in range(1, n+1, 1):
        total = total + k
    return total

a = input('음이 아닌 n값을 입력하세요:')
while not a.isdigit():
    a = input('음이 아닌 n값을 입력하세요:')
a = int(a)

print(f'1부터 {a}까지의 합은 {sum2n(a)}입니다.')
