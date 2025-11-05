import random
lotto = list(range(1,46))
#lotto = [i for i in range(1, 46)]
result = [] # 6개 보관 리스트
temp = 0 # 값 하나 임시 저장

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)
result_str = result_str + " / " + str(temp)

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)
result_str = result_str + "/" + str(temp)

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)
result_str = result_str + "/" + str(temp)

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)
result_str = result_str + "/" + str(temp)

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)
result_str = result_str + "/" + str(temp)

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)
result_str = result_str + "/" + str(temp)

print(f"{result[0]}/{result[1]}/{result[2]}/{result[3]}/{result[4]}/{result[5]}")
print(result_str)
print("temp :", temp)
print("result :", result)
print("lotto :", lotto)
