korean = int(input("국어 성적을 입력해주세요:"))
english = int(input("영어 성적을 입력해주세요:"))

result = int((korean+english)/2)

if(result >= 90):
    print(f"국어:{korean}점,영어:{english}점,평균:{result},우수상")
