Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> inqut()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    inqut()
NameError: name 'inqut' is not defined. Did you mean: 'input'?
>>> inqut
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    inqut
NameError: name 'inqut' is not defined. Did you mean: 'input'?
>>> input
<built-in function input>
>>> input()
5
'5'
>>> days=input()
5
>>> days
'5'
>>> 5+days
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    5+days
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5+int(days)
10
>>> input()
innput('나이를 입력하세요')
"innput('나이를 입력하세요')"
>>> input('나이를 입력하세요')
나이를 입력하세요19
'19'
>>> days=input('일수를 입력하세요')
일수를 입력하세요5
>>> days
'5'
>>> days=int(input('일수를 입력하세요:'))
일수를 입력하세요:5
>>> days
5
>>> 
======================= RESTART: C:/Users/user/Desktop/10518 최영은_0906_7.py =======================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10518 최영은_0906_7.py", line 4, in <module>
    print(str(a) + "+" + str(b)+"=" + str(a+b))
NameError: name 'a' is not defined
>>> 
======================= RESTART: C:/Users/user/Desktop/10518 최영은_0906_7.py =======================
8+5=13
>>> 
======================= RESTART: C:/Users/user/Desktop/10518 최영은_0906_7.py =======================
첫번째 숫자 입력:8
두번째 숫자 입력:5
8+5=85
>>> 
======================= RESTART: C:/Users/user/Desktop/10518 최영은_0906_7.py =======================
첫번째 숫자 입력:7
두번째 숫자 입력:3
7+3=10
