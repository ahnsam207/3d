file_data=open("data.txt","r",encoding = "utf-8")
data_list=file_data.readlines()
for d_I in data_list:
    print(d_I,end="")
file_data.close()
