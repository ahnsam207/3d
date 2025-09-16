Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
input()
5
'5'
days=input()
5
days
'5'
5+days
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    5+days
TypeError: unsupported operand type(s) for +: 'int' and 'str'
5+int(days)
10
input()

''
input('나이를 입력하세요:')
나이를 입력하세요:19
'19'
days=inpyt('일수록 입력하세요.')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    days=inpyt('일수록 입력하세요.')
NameError: name 'inpyt' is not defined. Did you mean: 'input'?
days=inpyt('일수를 입력하세요.')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    days=inpyt('일수를 입력하세요.')
NameError: name 'inpyt' is not defined. Did you mean: 'input'?
days=input('일수를 입력하세요.')
일수를 입력하세요.
days
''
days=int(intput('일수를 입력하세요:'))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    days=int(intput('일수를 입력하세요:'))
NameError: name 'intput' is not defined. Did you mean: 'input'?
days=int(input('일수를 입력하세요:'))
일수를 입력하세요:
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    days=int(input('일수를 입력하세요:'))
ValueError: invalid literal for int() with base 10: ''
days
''
>>> 
====================================== RESTART: C:/Users/user/Desktop/10504남은서_0916_7.py ======================================
8+5=13
>>> 
Warning (from warnings module):
  File "C:/Users/user/Desktop/10504남은서_0916_7.py", line 1
    a=8('첫번째 숫자 입력:')
SyntaxWarning: 'int' object is not callable; perhaps you missed a comma?
>>> 
Warning (from warnings module):
  File "C:/Users/user/Desktop/10504남은서_0916_7.py", line 2
    b=5('두번째 숫자 입력:')
SyntaxWarning: 'int' object is not callable; perhaps you missed a comma?
>>> 
====================================== RESTART: C:/Users/user/Desktop/10504남은서_0916_7.py ======================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/10504남은서_0916_7.py", line 1, in <module>
    a=8('첫번째 숫자 입력:')
TypeError: 'int' object is not callable
>>> 
====================================== RESTART: C:/Users/user/Desktop/10504남은서_0916_7.py ======================================
첫번째 숫자 입력:8
두번째 숫자 입력:5
8+5=85
>>> 
====================================== RESTART: C:/Users/user/Desktop/10504남은서_0916_7.py ======================================
첫번째 숫자 입력:7
두번째 숫자 입력:3
7+3=10
