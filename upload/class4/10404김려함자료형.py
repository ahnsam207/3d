Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> type(7)
<class 'int'>
>>> type(7.5)
<class 'float'>
>>> type("경복")
<class 'str'>
>>> type(7.5)
<class 'float'>
>>> 5+"7"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    5+"7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5+int
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    5+int
TypeError: unsupported operand type(s) for +: 'int' and 'type'
>>> 5+int("7")
12
>>> "7.5"
'7.5'
>>> float("7.5")
7.5
>>> 5+f1oat
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    5+f1oat
NameError: name 'f1oat' is not defined. Did you mean: 'float'?
>>> str(int(int(f1oat('3.5'))*3.5)
