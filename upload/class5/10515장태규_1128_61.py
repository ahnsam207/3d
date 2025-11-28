file_data = open("data.txt", "w", encoding = "utf-8")

data_list = ["30101,강하나,80,90\n","30102,kimiben,75,85\n","30103,nasamben,85,95"]

file_data.wirtelines(data_list)

file_data.close()
