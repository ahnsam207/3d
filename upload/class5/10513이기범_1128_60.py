file_data=open("data.txt","w")

data_list = ["10513,이기범,75,80,90\n", "10505,박광길,75,85,80\n", "10517,정호준,90,85,95\n"]

file_data.writelines(data_list)                                                             

file_data.close()
