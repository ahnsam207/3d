num1 = int(input("num1 input:"))
num2 = int(input("num2 input:"))

짝합 = 0
홀합 = 0
짝수 = 0
홀수 = 0

짝수들 = []
홀수들 = list()

for i in range(num1,num2+1):
    if i % 2 == 0:
        짝합 = 짝합+i
        짝수 = 짝수 +1
        짝수들.append(i)
    else:
        홀합 = 홀합 + i
        홀수 = 홀수 + 1
        홀수들.append(i)

print(f"{num1}~{num2}:짝수합-{짝합}, 홀수합-{홀합}, 짝수-{짝수}개, 홀수-{홀수}개")
print(f"짝수:{짝수들}")
print(f"홀수:{홀수들}")
