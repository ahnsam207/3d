Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> tpye(7)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    tpye(7)
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
>>> type(7)
<class 'int'>
>>> type(7.5)
<class 'float'>
>>> type("경복")
<class 'str'>
>>> 5+"7"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    5+"7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 5+int("7")
12
>>> 5+float("7.5")
12.5
>>> int(float("3.5")+3)+5
11
>>> int(float("3.5")+8)+5
16
>>> str(int(int(float("3.5"))*3.5)
