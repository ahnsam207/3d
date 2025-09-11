Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> K3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    K3
NameError: name 'K3' is not defined
>>> K3 = 7
>>> K3
7
>>> K5 = "5"
>>> K5
'5'
>>> type(K3)
<class 'int'>
>>> type(K5)
<class 'str'>
>>> K7 = 7.5
>>> K7
7.5
>>> type(K7)
<class 'float'>
>>> K3
7
>>> K7
7.5
>>> K5
'5'
>>> K3 = K3 = 3
>>> K3 = K3 +3
>>> K3
6
>>> K3 = 7
>>> K5 + "5"
'55'
>>> K3 = 7
>>> K5 = "5"
>>> K7 = 7.5
>>> K3 = K3 + 3
>>> K3
10
>>> K3 = K3 + imt(K5)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    K3 = K3 + imt(K5)
NameError: name 'imt' is not defined. Did you mean: 'int'?
>>> K3 = K3 + int(K5)
>>> K3
15
