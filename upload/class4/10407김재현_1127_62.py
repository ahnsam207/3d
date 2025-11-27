file_data = open("data.txt", "r", encoding = "utf=8")
data_list =["10407,김재현","파이썬재미있다","너무재미있다"]
file_data.writelines(data_list)
file_data.close()
