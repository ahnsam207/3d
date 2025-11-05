import random

lotto=list(range(1,46))
#lotto=[i for i in range(1,46)]

temp=0
result =[]

temp=random.choice(lotto)
result.append(temp)
lotto.remove(temp)

temp=random.choice(lotto)
result.append(temp)
lotto.remove(temp)

temp=random.choice(lotto)
result.append(temp)
lotto.remove(temp)

temp=random.choice(lotto)
result.append(temp)
lotto.remove(temp)

temp=random.choice(lotto)
result.append(temp)
lotto.remove(temp)

temp=random.choice(lotto)
result.append(temp)
lotto.remove(temp)

print("temp : ", temp)
print("result :" , result)
print("lotto :",lotto)

print(f"{result[0]}/{result[1]}/{result[2]}/{result[3]}/{result[4]}/{result[5]}")


