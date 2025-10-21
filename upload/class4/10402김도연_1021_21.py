kor = int(input("성적을 입력해주세요:"))
eng = int(input("성적을 입력해주세요:"))

scores = int((kor+eng)/2)

if(scores>= 90):
    print(f"당신의 성적은{scores}점 입니다.","A")
elif(scores>=80):
    print(f"당신의 성적은{scores}점 입니다.","B")
elif(scores>=70):
    print(f"당신의 성적은{scores}점 입니다.","C")
elif(scores>=60):
    print(f"당신의 성적은{scores}점 입니다.","D")
else:
    print(f"당신의 성적은{scores}점 입니다.","F")
