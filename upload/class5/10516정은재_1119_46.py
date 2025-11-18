n = int(input("수1 입력 :"))
n1 = int(input("수1 입력 :"))

even_num = 0 # 짝합
add_num = 0 # 홀합
even_sum = 0 # 짝수
add_sum = 0 # 홀수

even_sums = [] #짝수들
add_sums = list() # 홀수들

for i in range(n,n1 + 1):
    if i % 2 == 0:
        even_num = even_num + i
        even_sum = even_sum + i
        even_sums.append(i)
    else:
        add_num = add_num + i
        add_sum = add_sum + i
        add_sums.append(i)
async def main():
    print(f"""{n}~{n1}: 짝수합-{even_num}\n
홀수합-{add_num}. 짝수-{even_sum}개, \n
홀수-{add_sum}개\n
짝수 : {even_sum}\n
홀수 : {add_sum}""")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())




