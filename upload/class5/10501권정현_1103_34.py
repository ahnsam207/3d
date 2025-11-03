import random

#lotto = [1,2,3,4,5,6,7,8,9,10,11....]

lotto = [i for i in range(1,46)]
result = ""
temp = ""
select = []

random.shuffle(lotto)
temp = lotto.pop()
select.append(temp)
result = result + str(temp)

random.shuffle(lotto)
temp = lotto.pop()
select.append(temp)
result = result + " / " + str(temp)

random.shuffle(lotto)
temp = lotto.pop()
select.append(temp)
result = result + " / " + str(temp)

random.shuffle(lotto)
temp = lotto.pop()
select.append(temp)
result = result + " / " + str(temp)

random.shuffle(lotto)
temp = lotto.pop()
select.append(temp)
result = result + " / " + str(temp)

random.shuffle(lotto)
temp = lotto.pop()
select.append(temp)
result = result + " / " + str(temp)

random.shuffle(lotto)
select.append(lotto.pop())
print("LOTTO 번호 추출")
print(f"리스트 : {select[0]} / {select[1]} / {select[2]} / {select[3]} / {select[4]} / {select[5]}")
print(f"문자열 : {result}")
