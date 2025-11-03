import random


lotto = [i for i in range(1,46)]



result = ""
select = []
random.shuffle(lotto)

print("=" * 10 + "lotto" + "=" * 10)
print(lotto)


select.append(lotto.pop())
print("=" * 10 + "new_lotto" + "=" * 10)
#print(select)

lotto_repeat = 0
print(lotto)


while lotto_repeat < 6:
              
    lotto_repeat += 1
    random.shuffle(lotto)
    select.append(lotto.pop())
    #print(lotto_repeat)
        


print("=" * 10  + "=" * 10)
print(f"{select[0]} / {select[1]} / {select[2]} / {select[3]} /{select[4]} /{select[5]}")
print("=" * 10  + "=" * 10)
#print(select)
#print(lotto_repeat)
