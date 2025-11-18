Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:/Users/user/Desktop/10513이기범_1118_45.py ==============
반복 횟수:7
값 입력1
v:1,c:1,s:1
값 입력2
v:2,c:2,s:3
값 입력4
v:4,c:3,s:7
값 입력5
v:5,c:4,s:12
값 입력6
v:6,c:5,s:18
값 입력7
v:7,c:6,s:25
값 입력8
v:8,c:7,s:33

============== RESTART: C:/Users/user/Desktop/10513이기범_1118_46.py ==============
수1 입력:7
수2 입력:8
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10513이기범_1118_46.py", line 15, in <module>
    짝수=짝수+i
NameError: name '짝수' is not defined. Did you mean: '짯수'?

============== RESTART: C:/Users/user/Desktop/10513이기범_1118_46.py ==============
수1 입력:9
수2 입력:8
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10513이기범_1118_46.py", line 22, in <module>
    print(f"{수1}~{수2}:짝수합-{짝합},홀수합-{홀합},짝수~{짝수}개,홀수~{홀수}개")
NameError: name '짝수' is not defined. Did you mean: '짯수'?
>>> studunt={'학번':2025,'소속:'AI','이름':'김경복'}
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> student['이름']
...          
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    student['이름']
NameError: name 'student' is not defined
>>> student['학년']=2
...          
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    student['학년']=2
NameError: name 'student' is not defined
>>> student
...          
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    student
NameError: name 'student' is not defined
>>> del studnt['소속']
...          
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    del studnt['소속']
NameError: name 'studnt' is not defined
>>> f"내 이름은 {student[이름]}, 학년은 {student[학년]}학년 입니다."
...          
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    f"내 이름은 {student[이름]}, 학년은 {student[학년]}학년 입니다."
NameError: name 'student' is not defined
