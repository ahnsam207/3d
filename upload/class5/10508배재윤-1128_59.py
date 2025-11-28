file_data = open("data.txt", "w" ,encoding= "utf-8")

data_list = ["10508,qowodbs|n,88,55,66","10509,이지안,89,56"]
file_data.writelines(data_list)
file_data.close()
