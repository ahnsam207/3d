korean = int(input("korean score:"))
english = int(input("english score:"))

score = (korean+english)/2

result = round(score,1)

print(f"당신의 평균은 {result} 입니다.")
print("당신의 평균은",result,"입니다.")
print("당신의 평균은 "+str(result)+" 입니다.")
