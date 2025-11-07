import random
lotto = [i for i in range(1,46)]
select = []

random.shuffle(lotto)

for i in range(6):
    select.append(lotto.pop())
print(select)
