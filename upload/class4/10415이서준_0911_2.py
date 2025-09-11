Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> k3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    k3
NameError: name 'k3' is not defined
>>> k3=7
>>> k3
7
>>> k5=5
>>> k5
5
>>> a=3
>>> a
3
>>> type(k7)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(k7)
NameError: name 'k7' is not defined. Did you mean: 'k3'?
>>> type(k7)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(k7)
NameError: name 'k7' is not defined. Did you mean: 'k3'?
>>> type(k3)
<class 'int'>
>>> 10415이서준생년월일='2009년04월19일'
SyntaxError: invalid syntax
>>> 10415='이서준'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> '10415이서준생년월일'='2009년04월19일'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
