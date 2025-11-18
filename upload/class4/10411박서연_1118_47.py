Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============== RESTART: C:/Users/user/Desktop/10411박서연_1118_45.py ==============
반복 횟수: 5
값 입력: 5
v:5, c:1, s:5
값 입력: 3
v:3, c:2, s:8
값 입력: 10
v:10, c:3, s:18
값 입력: 56
v:56, c:4, s:74
값 입력: 58
v:58, c:5, s:132

============== RESTART: C:/Users/user/Desktop/10411박서연_1118_45.py ==============
반복 횟수: 10
값 입력: 1
v:1, c:1, s:1
값 입력: 2
v:2, c:2, s:3
값 입력: 3
v:3, c:3, s:6
값 입력: 4
v:4, c:4, s:10
값 입력: 5
v:5, c:5, s:15
값 입력: 6
v:6, c:6, s:21
값 입력: 7
v:7, c:7, s:28
값 입력: 8
v:8, c:8, s:36
값 입력: 9
v:9, c:9, s:45
값 입력: 10
v:10, c:10, s:55

============== RESTART: C:/Users/user/Desktop/10411박서연_1118_45.py ==============
반복 횟수: 10
값 입력: 11
v:11, c:1, s:11
값 입력: 12
v:12, c:2, s:23
값 입력: 13
v:13, c:3, s:36
값 입력: 14
v:14, c:4, s:50
값 입력: 15
v:15, c:5, s:65
값 입력: 16
v:16, c:6, s:81
값 입력: 17
v:17, c:7, s:98
값 입력: 18
v:18, c:8, s:116
값 입력: 19
v:19, c:9, s:135
값 입력: 2
v:2, c:10, s:137
0
============== RESTART: C:/Users/user/Desktop/10411박서연_1118_45.py ==============
반복 횟수: 3
값 입력: 1
v:1, c:1, s:1
값 입력: 2
v:2, c:2, s:3
값 입력: 3
v:3, c:3, s:6

============== RESTART: C:/Users/user/Desktop/10411박서연_1118_46.py ==============
수1 입력: 1
수2 입력: 6
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10411박서연_1118_46.py", line 22, in <module>
    print(f"{수1}~{수2}: 짝수합 - {짝수합}, 홀수합 - {홀수합}, 짝수 - {짝수}, 홀수 - {홀수}개")
NameError: name '짝수합' is not defined. Did you mean: '짝합'?
>>> 
============== RESTART: C:/Users/user/Desktop/10411박서연_1118_46.py ==============
수1 입력: 1
수2 입력: 6
1~6: 짝수합 - 0, 홀수합 - 6, 짝수 - 0, 홀수 - 6개
짝수: []
홀수: [1, 1, 1, 1, 1, 1]
>>>  student = {"학번": 2025, "소속": "AI", "이름": "김경복"}
...  
SyntaxError: unexpected indent
>>> student = {"학번": 2025, "소속": "AI", "이름": "김경복"}
>>> stundent
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    stundent
NameError: name 'stundent' is not defined. Did you mean: 'student'?
>>> student["이름"]
'김경복'
>>> student["학년"] = 1
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 1}
>>> student["학년"] = 2
>>> student
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
>>> del student["소속"]
>>> student
{'학번': 2025, '이름': '김경복', '학년': 2}
>>> f"내 이름은 {student["이름"]}, 학년은 {student["학년"]}학년 입니다."
'내 이름은 김경복, 학년은 2학년 입니다.'
