Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> type(7)
<class 'int'>
>>> type(7.5)
<class 'float'>
>>> type("경복")
<class 'str'>
>>> type("7.5")
<class 'str'>
>>> 5+7
12
>>> 5 + "7"
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    5 + "7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 
>>> 5 + int("7")
12
>>> "7.5"
'7.5'
>>> float("7.5")
7.5
>>> 5 + float("7.5")
12.5
>>> +12
12
>>> int(10.7)
10
>>> int(folat('3.5')*3) + 5
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(folat('3.5')*3) + 5
NameError: name 'folat' is not defined. Did you mean: 'format'?
>>> int(float('3.5')*3)+5
15
0b1010
10
0b11010
26
0o34
28
0xA1
161
000001
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
000010
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
010001
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
str(int(int(float('3.5'))*3.5))
'10'
