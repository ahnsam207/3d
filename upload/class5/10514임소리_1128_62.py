file_data = open('data.txt', 'r', encoding = 'utf-8')

data_list = file_data.readlines()

for d_l in data_list:
    print(d_l, end ='')
file_data.close()
