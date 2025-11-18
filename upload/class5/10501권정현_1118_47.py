Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:/Users/user/Desktop/10501권정현_1118_45.py ==============
반복 횟수:
============== RESTART: C:/Users/user/Desktop/10501권정현_1118_45.py ==============
반복 횟수:6
값 입력2
v: 2, c : 1, s: 2
값 입력2
v: 2, c : 2, s: 4
값 입력3
v: 3, c : 3, s: 7
값 입력6
v: 6, c : 4, s: 13
값 입력
============== RESTART: C:/Users/user/Desktop/10501권정현_1118_46.py ==============
수1 입력7
수2 입력17
7~17 : 짝수합-60, 홀수합-55, 짝수-5개, 홀수-5개
짝수 : [8, 10, 12, 14, 16]
홀수 : [7, 9, 11, 13, 15]
짝수 : [8, 10, 12, 14, 16]
student = {'학번':2025, '소속':'AI', '이름' : '김경복'}
student['이름']
'김경복'
student
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
student['학번'] = 1
student
{'학번': 1, '소속': 'AI', '이름': '김경복'}
>>> student['학번'] = 2
>>> student
{'학번': 2, '소속': 'AI', '이름': '김경복'}
>>> del student['소속']
>>> student
{'학번': 2, '이름': '김경복'}
>>> f"내 이름은 {student['이름']}, 학년은 {student['학년']}학년 입니다."
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f"내 이름은 {student['이름']}, 학년은 {student['학년']}학년 입니다."
KeyError: '학년'
>>>  f"내 이름은  {student [ '이름' ] },  학년은  {student[ '학년' ] }학년 입니다."
...  
SyntaxError: unexpected indent
>>> f"내 이름은  {student [ '이름' ] },  학년은  {student[ '학년' ] }학년 입니다."
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    f"내 이름은  {student [ '이름' ] },  학년은  {student[ '학년' ] }학년 입니다."
KeyError: '학년'
>>> f"내 이름은  {student [ '이름' ] },  학년은  {student [ '학년' ] }학년 입니다."
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    f"내 이름은  {student [ '이름' ] },  학년은  {student [ '학년' ] }학년 입니다."
KeyError: '학년'
