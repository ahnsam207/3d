import random

lotto = list(range(1,46))

result = ""
random.shuffle(lotto)
result = result + " / " + str(lotto.pop())

random.shuffle(lotto)
result = result + " / " + str(lotto.pop())

random.shuffle(lotto)
result = result + " / " + str(lotto.pop())

random.shuffle(lotto)
result = result + " / " + str(lotto.pop())

random.shuffle(lotto)
result = result + " / " + str(lotto.pop())

random.shuffle(lotto)
result = result + " / " + str(lotto.pop())

print(result)

