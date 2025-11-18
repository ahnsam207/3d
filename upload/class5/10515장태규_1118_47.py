Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:/Users/user/Desktop/10515장태규_1118_45.py ==============
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10515장태규_1118_45.py", line 4, in <module>
    a = inut('반복 횟수:')
NameError: name 'inut' is not defined. Did you mean: 'input'?

============== RESTART: C:/Users/user/Desktop/10515장태규_1118_45.py ==============
반복 횟수:45
값 입력:45
v:45,c:1,s:45
값 입력:45
v:45,c:2,s:90
값 입력:45
v:45,c:3,s:135
값 입력:45
v:45,c:4,s:180
값 입력:45
v:45,c:5,s:225
값 입력:45
v:45,c:6,s:270
값 입력:45
v:45,c:7,s:315
값 입력:45
v:45,c:8,s:360
값 입력:45
v:45,c:9,s:405
값 입력:45
v:45,c:10,s:450
값 입력:45
v:45,c:11,s:495
값 입력:45
v:45,c:12,s:540
값 입력:45
v:45,c:13,s:585
값 입력:45
v:45,c:14,s:630
값 입력:45
v:45,c:15,s:675
값 입력:45
v:45,c:16,s:720
값 입력:45
v:45,c:17,s:765
값 입력:45
v:45,c:18,s:810
값 입력:45
v:45,c:19,s:855
값 입력:45
v:45,c:20,s:900
값 입력:45
v:45,c:21,s:945
값 입력:45
v:45,c:22,s:990
값 입력:10
v:10,c:23,s:1000
값 입력:45
v:45,c:24,s:1045
값 입력:45
v:45,c:25,s:1090
값 입력:4
v:4,c:26,s:1094
5값 입력:4
v:4,c:27,s:1098
값 입력:54
v:4,c:28,s:1102
값 입력:54
v:54,c:29,s:1156
값 입력:54
v:54,c:30,s:1210
값 입력:5
v:5,c:31,s:1215
4값 입력:5
v:5,c:32,s:1220
값 입력:45
v:45,c:33,s:1265
값 입력:4
v:4,c:34,s:1269
값 입력:54
v:54,c:35,s:1323
값 입력:5
v:5,c:36,s:1328
4값 입력:5
v:5,c:37,s:1333
값 입력:45
v:45,c:38,s:1378
값 입력:45
v:45,c:39,s:1423
값 입력:43
v:43,c:40,s:1466
5값 입력:234
v:234,c:41,s:1700
6값 입력:234
v:234,c:42,s:1934
값 입력:654
v:654,c:43,s:2588
값 입력:y54
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10515장태규_1118_45.py", line 9, in <module>
    v = int(input('값 입력:'))
ValueError: invalid literal for int() with base 10: 'y54'
6
>>> 54
>>> 6
6
54
>>> 
============== RESTART: C:/Users/user/Desktop/10515장태규_1118_46.py ==============
수1 입력:2
수2 입력:3
2~3:짝수합-2, 홀수합-3, 짝수-1개, 홀수-1개
짝수:[2]
홀수:[3]
>>> student = {'학번':2025, '소속':'AI', '이름':'김경복'}
>>> student['이름']
'김경복'
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
>>> student['학년'] = 1
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 1}
>>> student['학년'] = 2
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
>>> del student['소속']
>>> student
{'학번': 2025, '이름': '김경복', '학년': 2}
>>> f'내 이름은 {STUDENT['이름']}, 학년은 {student['학년']}학년 입니다.'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    f'내 이름은 {STUDENT['이름']}, 학년은 {student['학년']}학년 입니다.'
NameError: name 'STUDENT' is not defined
>>> f"내 이름은 {student['이름']}, 학년은 [student['학년']}학년 입니다."
SyntaxError: f-string: single '}' is not allowed
>>> f"내 이름은 {student['이름']}, 학년은 [student['학년']}학년 입니다."
SyntaxError: f-string: single '}' is not allowed
>>> f"내 이름은 {student['이름']}, 학년은 [student['학년']학년 입니다."
"내 이름은 김경복, 학년은 [student['학년']학년 입니다."
