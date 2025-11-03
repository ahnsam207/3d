import random

#lotto = [1,2,3,4,5,6,7,8,9,10,11......]
lotto = [i for i in range(1,46)]
result = ""
tiemp = ""
select = []

random.shuffle(lotto)

print("="* 10 + "lotto" + "=" *10)
print(lotto)

select.append(lotto.pop())
print("="* 10 + "select" + "=" *10)
print(select)
print("="* 10 + "new_lotto" + "=" *10)
print(lotto)

random.shuffle(lotto)
select.append(lotto.pop())

random.shuffle(lotto)
select.append(lotto.pop())

random.shuffle(lotto)
select.append(lotto.pop())

random.shuffle(lotto)
select.append(lotto.pop())

random.shuffle(lotto)
select.append(lotto.pop())

print("lotto 번호 추출")
print(f"{select[0]}/ {select[1]}/ {select[2]}/ {select[3]}/ {select[4]}/ {select[5]}/")


