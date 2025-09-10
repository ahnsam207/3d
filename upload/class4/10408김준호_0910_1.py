Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> type(7)
<class 'int'>
>>> tyep(7.5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tyep(7.5)
NameError: name 'tyep' is not defined
>>> type(7.5)
<class 'float'>
>>> type("경복")
<class 'str'>
>>> 5 + "7"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    5 + "7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5 + int("7")
12
>>> "7.5"
'7.5'
>>> float("7.5")
7.5
>>> 5 + float("7.5")
12.5
>>> int (10.7)
10
>>> int(float('3.5')*3) + 5
15
>>> 0b1010
10
>>> 0b11010
26
>>> 0o34
28
>>> 0xa1
161
>>> str(int(int(float('3.5'))*3.5))
'10'
