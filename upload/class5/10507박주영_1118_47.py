Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:/Users/user/Desktop/10507박주영_1118_45.py ==============
반복 횟수:6
값 입력:2
v:2,c:1,s:2
값 입력:
============== RESTART: C:/Users/user/Desktop/10507박주영_1118_45.py ==============
반복 횟수:3
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10507박주영_1118_45.py", line 7, in <module>
    for i in range(a):
TypeError: 'str' object cannot be interpreted as an integer
>>> 
============== RESTART: C:/Users/user/Desktop/10507박주영_1118_45.py ==============
반복 횟수:3
값 입력:1
v:1,c:1,s:1
값 입력:1
v:1,c:2,s:2
값 입력:1
v:1,c:3,s:3
>>> 1
1
>>> 
============== RESTART: C:/Users/user/Desktop/10507박주영_1118_46.py ==============
수1 입력:7
수2 입력:17
7~17:짝수합-5, 홀수합-6, 짝수-5개, 홀수-6개
짝수:[8, 10, 12, 14, 16]
홀수:[7, 9, 11, 13, 15, 17]
>>> student = {"학번":2025, "소속":"AI", "이름":"김경복"}
>>> student["이름"]
'김경복'
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
>>> student["학년"] = 1
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 1}
>>> student["학년"] = 2
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
>>> del student["소속"]
>>> student
{'학번': 2025, '이름': '김경복', '학년': 2}
>>> f"내 이름은 {student['이름']}, 학년은 {student['학년']} 학년 입니다."
'내 이름은 김경복, 학년은 2 학년 입니다.'
