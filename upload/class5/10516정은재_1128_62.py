FILE_DATA = open("data.txt","r",encoding="utf-8")

DATA_LIST = FILE_DATA.readlines()

for d_I in DATA_LIST:
    print(d_I,end="")
FILE_DATA.close()
