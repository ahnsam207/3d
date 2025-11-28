file_data = open ('data.txt','r',encoding='utf-8')
data_list = file_data.readllines()
for d_l in dta_list:
    print(d_l, end = "")
file_data.close()
