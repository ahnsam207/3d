Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> k3=7
>>> k3
7
>>> type(k3)
<class 'int'>
>>> k5+"5"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    k5+"5"
NameError: name 'k5' is not defined. Did you mean: 'k3'?
>>> k5="5"
>>> K5
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    K5
NameError: name 'K5' is not defined. Did you mean: 'k5'?
>>> k5
'5'
>>> type(k5)
<class 'str'>
>>> k7
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    k7
NameError: name 'k7' is not defined. Did you mean: 'k3'?
>>> k7=7.5
>>> k7
7.5
>>> k3
7
>>> k5
'5'
>>> k7
7.5
>>> k3=k3+3
>>> k3
10
>>> k3=k3+int("7")
>>> k3
17
>>> k3=k3+int(k5)
>>> k3
22
