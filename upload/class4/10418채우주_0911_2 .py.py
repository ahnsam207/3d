Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> k3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    k3
NameError: name 'k3' is not defined
>>> k3 = 7
>>> k3
7
>>> k5 = 5
>>> k5
5
>>> type(k3)
<class 'int'>
>>> type(k5)
<class 'int'>
>>> k7 = 7.5
>>> type(k7)
<class 'float'>
>>> k5 = '5'
>>> type(k5)
<class 'str'>
>>> k3
7
>>> k5
'5'
>>> k7
7.5
>>> k3 = k3 + int(k5)
>>> k3
12
