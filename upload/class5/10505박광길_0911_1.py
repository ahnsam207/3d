Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
    type(7)
    
SyntaxError: unexpected indent
type(7)
<class 'int'>
type(7.5)
<class 'float'>
>>> type("대성")
<class 'str'>
>>> type('7,5')
<class 'str'>
>>> type("7")
<class 'str'>
>>> 5+3
8
>>> 5+"7"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    5+"7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5+int("7")
12
>>> 999999+99999999999
100000999998
>>> "7"
'7'
>>> int("7")
7
>>> int(7.5)
7
>>> float("7,5)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> float(5)
...       
5.0
>>> 5+6.5
...       
11.5
>>> int(float("3,5")*3)
...       
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(float("3,5")*3)
ValueError: could not convert string to float: '3,5'
>>> int(float("3.5)*3)
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> str(int(int(int(float("3.5"))*3.5))
... 
