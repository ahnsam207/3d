file_data = open("data.txt","w",encoding="utf-8")

data_list = ["10101,강하나,75,80,90","10102,김이범,75,85,80","10103나삼번,90,85,95"]

file_data.writelines(data_list)

file_data.close

