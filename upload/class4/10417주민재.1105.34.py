import random
lotto = list(range(1,46))
result = []
temp = 0

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)

temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)


temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)


temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)


temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)


temp = random.choice(lotto)
result.append(temp)
lotto.remove(temp)

print(f"{result[0]},{result[1]},{result[2]},{result[3]},{result[4]},{result[5]}")
