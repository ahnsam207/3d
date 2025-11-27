file_data=open("data.txt","w", encoding="utf-8")

data_list = ["10401,김단풍, 75, 80, 90", "10402,김태풍,75,80,90", "10403,김폭풍,90,85,95"]

file_data.writelines(data_list)

file_data.close()
