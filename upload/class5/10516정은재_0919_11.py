class logger:
    def info(msg:str):
        print(msg)


hou = int(input("면적 입력(제곱미터):"))

hou_y = hou * 0.325
hou_x = round(0.325 * hou_y,1)

print(int(hou))


