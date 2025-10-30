k_num = input("학번 입럭 : ")
k_name = input("성명 입력 : ")

kgra = k_name[0]

gra = k_num[1:3]
k_only_num = k_num[3:len(k_num)]

first_n = k_name[0]
last_n =k_name[1:len(k_name)]

print(f'{kgra} 학년 {gra}반 {k_only_num}번 \n 성: {first_n} 이름 : {last_n}')


