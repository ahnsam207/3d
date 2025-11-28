file_data = open("data.txt","w", encoding = "utf-8")

data_list= ["10101,강하나,75,80,90\n","10102,김이번,75,85,80\n","10103,나삼번,90,85,95\n"]

file_data.writelines(data_list)

file_data.close()
