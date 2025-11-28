FILE_DATA = open("data.txt","w")

DATA_LIST = ["10101, 한글,75,80,90\n","10101, 한글,75,80,90\n","10101, 한글,75,80,90\n"]



FILE_DATA.writelines(DATA_LIST)



FILE_DATA.close()
