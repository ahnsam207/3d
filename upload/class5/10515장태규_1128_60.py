file_data = open("data.txt" , "w" ,encoding = "utr-8")

data_list = ["10515,장태규,75,80,90", "10517,정호준,75,85,80", "10505,박광길,90,85,95"]

file_data.writelines(data_list)

file_data.close()
