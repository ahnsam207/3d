Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:/Users/user/Desktop/10510심대성_1118_45.py ==============
반복 횟수 :10
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10510심대성_1118_45.py", line 5, in <module>
    while not a.insdigit() :
AttributeError: 'str' object has no attribute 'insdigit'. Did you mean: 'isdigit'?

============== RESTART: C:/Users/user/Desktop/10510심대성_1118_45.py ==============
반복 횟수 :15
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10510심대성_1118_45.py", line 5, in <module>
    while not a.insdigit() :
AttributeError: 'str' object has no attribute 'insdigit'. Did you mean: 'isdigit'?

============== RESTART: C:/Users/user/Desktop/10510심대성_1118_45.py ==============
반복 횟수 :20
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10510심대성_1118_45.py", line 5, in <module>
    while not a.insdigit() :
AttributeError: 'str' object has no attribute 'insdigit'. Did you mean: 'isdigit'?

============== RESTART: C:/Users/user/Desktop/10510심대성_1118_45.py ==============
반복 횟수 :3
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10510심대성_1118_45.py", line 5, in <module>
    while not a.insdigit() :
AttributeError: 'str' object has no attribute 'insdigit'. Did you mean: 'isdigit'?

============== RESTART: C:/Users/user/Desktop/10510심대성_1118_45.py ==============
반복 횟수 :3
값 입력:3
v:3,c:1,s:3
값 입력:3
v:3,c:2,s:6
값 입력:1
v:1,c:3,s:7
4
4
>>> 
============== RESTART: C:/Users/user/Desktop/10510심대성_1118_46.py ==============
수1 입력:3
수2 입력:3
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10510심대성_1118_46.py", line 22, in <module>
    print(f"{수}~{수2}:짝수합-{짝합}, 홀수합-{홀합}, 짝수-{짝수}개, 홀수-{홀수}개")
NameError: name '수' is not defined. Did you mean: '수1'?
>>> student = {'학번':2025, '소속':'AI', '이름':'김경복'}
>>> student = ['이름']
>>> student = ['이름']
>>> 
>>> student = {'학번':2025, '소속':'AI', '이름':'김경복'}
... student['이름']
SyntaxError: multiple statements found while compiling a single statement
>>> student = {'학번':2025, '소속':'AI', '이름':'김경복'}
>>> student['이름']
'김경복'
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
>>> student['학년'] = 1
>>> ㄴ셩둣
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ㄴ셩둣
NameError: name 'ᄂ셩둣' is not defined
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 1}
>>> student['학년'] = 2
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
>>> del student['소속']
>>> student
{'학번': 2025, '이름': '김경복', '학년': 2}
>>> f"내 이름은 {student['이름']}, 학년은 {student['학년']}학년 입니다."
'내 이름은 김경복, 학년은 2학년 입니다.'
