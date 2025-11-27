file_data = open("data.txt","w", encoding = "utf-8")


data_list = ["10417주민재,09,03,25/n"]

file_data.writelines(data_list)

file_data.close()
