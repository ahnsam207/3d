file_data = open("data.txt", "w", encoding = "utf-8")

data_list = ["10415,이서준","파이썬재미있다.","러랴러댤ㄷㅈ랴ㅓ"]
file_data.writelines(data_list)
file_data.close()
