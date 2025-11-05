import random

lotto=list(range(1,46))
temp=0
result=""
random.shuffle(lotto)
result=result+str(lotto.pop())

random.shuffle(lotto)
result=result+" / "+str(lotto.pop())

random.shuffle(lotto)
result=result+" / "+str(lotto.pop())

random.shuffle(lotto)
result=result+" / "+str(lotto.pop())

random.shuffle(lotto)
result=result+" / "+str(lotto.pop())

random.shuffle(lotto)
result=result+" / "+str(lotto.pop())
print(f" {result} ")
