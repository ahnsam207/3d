import random
lotto = [i for i in range(1,46)]
select = []

random.shuffle(lotto)

while len(select) < 6:
    select.append(lotto.pop())
print(select)
