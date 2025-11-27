file_data=open("data.txt","w", encoding = "utf-8")

data_list=["10413,안재훈,75,80,90","10413-2,안재훈-2,75,85,80","10413-3,안재훈-3,90,85,95"]

file_data.witelines(data_list)

file_data.close()
