Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
k3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    k3
NameError: name 'k3' is not defined
error
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    error
NameError: name 'error' is not defined. Did you mean: 'OSError'?
k3 = 7
k3
7
k5 = "5"
k5
'5'
>>> type k3
SyntaxError: invalid syntax
>>> type (k3)
<class 'int'>
>>> type (k5)
<class 'str'>
>>> k7 = 7.5
>>> k7
7.5
>>> type k7
SyntaxError: invalid syntax
>>> type (k7)
<class 'float'>
>>> k3
7
>>> k5
'5'
>>> k7
7.5
>>> k3 = k3 + 3
>>> k3
10
>>> k3 + int(k5)
15
>>> k3
10
>>> k3= int(k5) =
SyntaxError: cannot assign to function call
>>> k3 = int(k5) =
SyntaxError: cannot assign to function call
>>> stinger = k3
>>> k3
10
>>> stinger
10
>>> stinger = int(k5) + k3
>>> stinger
15
