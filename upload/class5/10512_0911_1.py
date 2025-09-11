Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> type(7)
<class 'int'>
>>> type(7.5)
<class 'float'>
>>> type("대성")
<class 'str'>
>>> type('7.5')
<class 'str'>
>>> 
>>> 5+"7"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    5+"7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5+int("7")
12
>>> int("7")
7
>>> int(7.9)
7
>>> float(7.5)
7.5
>>> float(5)
5.0
>>> 5+6.5
11.5
>>> 
>>> int(float("3.5")*3)
10
>>> 
>>> str(int(int(float("3.5"))*3.5))
'10'
