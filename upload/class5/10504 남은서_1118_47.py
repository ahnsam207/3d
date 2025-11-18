Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/10518 최영은_1118_45.py
반복 횟수: 2
값 입력: 2
v:2,c:1,s:2
값 입력: 1
v:1,c:2,s:3
4
4
5
5
96
96

= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/10518 최영은_1118_45.py
반복 횟수: 2
값 입력: 
= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/10518 최영은_1118_45.py
반복 횟수: 5
값 입력: 3
Traceback (most recent call last):
  File "C:/Users/user/AppData/Local/Programs/Python/Python313/10518 최영은_1118_45.py", line 11, in <module>
    s = s+v
TypeError: unsupported operand type(s) for +: 'int' and 'str'

= RESTART: C:/Users/user/AppData/Local/Programs/Python/Python313/10518 최영은_1118_45.py
반복 횟수: 5
값 입력: 2
v:2,c:1,s:2
값 입력: 1
v:1,c:2,s:3
값 입력: 3
v:3,c:3,s:6
값 입력: 4
v:4,c:4,s:10
값 입력: 6
v:6,c:5,s:16

============== RESTART: C:/Users/user/Desktop/10518 최영은_1118_46.py =============
수1 입력: 
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10518 최영은_1118_46.py", line 1, in <module>
    수1 = int(input("수1 입력: "))
ValueError: invalid literal for int() with base 10: ''
>>> 
============== RESTART: C:/Users/user/Desktop/10518 최영은_1118_46.py =============
수1 입력: 1
수2 입력: 2
1~2:짝수합-0, 홀수합-3, 짝수-0개,홀수-2개
짝수:[]
홀수:[1, 2]
>>> 
>>> 
>>> 
>>> student = {'학번':2025, '소속':'AI', '이름' : '김경복'}
>>> student['이름']
'김경복'
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
>>> student['학년'] =2
>>> studet
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    studet
NameError: name 'studet' is not defined. Did you mean: 'student'?
>>> stuednt
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    stuednt
NameError: name 'stuednt' is not defined. Did you mean: 'student'?
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
>>> del student['소속']
>>> student
{'학번': 2025, '이름': '김경복', '학년': 2}
>>> f"내 이름은 {student['이름']}, 학년은 {student['학년']}학년 입니다."
'내 이름은 김경복, 학년은 2학년 입니다.'
