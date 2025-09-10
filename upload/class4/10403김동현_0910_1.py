Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
type(7)
<class 'int'>
type(7.5)
<class 'float'>
type("경복")
<class 'str'>
type("7.5")
<class 'str'>
5 + int("7")
12
"7.5"
'7.5'
>>> float("7.5")
7.5
>>> 5 + float("7.5")
12.5
>>> int(10.7)
10
>>> it(float('3.5')*3) +5
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    it(float('3.5')*3) +5
NameError: name 'it' is not defined. Did you mean: 'id'?
>>> int(float('3.5')*3)+5
15
>>> 0b1010
10
>>> 
>>> 0b11010
26
>>> 0o
SyntaxError: invalid octal literal
>>> 0o34
28
>>> 0xa1
161
>>> 0xA1
161
>>> str(int(int(float('3.5'))*3.5))
'10'
