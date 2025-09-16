Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
input()
5
'5'
>>> days = input()
5
>>> days
'5'
>>> 5 + days
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    5 + days
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5 + int(days)
10
>>> input()

''
>>> input('나이를 입력하세요:' )
나이를 입력하세요:
''
>>> 나이를 입력하세요:19
SyntaxError: invalid syntax
>>> days = input('일수를 입력하세요. ')
일수를 입력하세요. 5
>>> days
'5'
>>> days = int(input('일수를 입력하세요:'))
일수를 입력하세요:5
>>> days
5
