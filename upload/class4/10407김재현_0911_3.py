Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> K3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    K3
NameError: name 'K3' is not defined
>>> K3=7
>>> K3
7
>>> K5="5"
>>> K5
'5'
>>> type(K3)
<class 'int'>
>>> type(K5)
<class 'str'>
>>> K7=7.5
>>> K7
7.5
>>> type(K7)
<class 'float'>
>>> K5
'5'
>>> K3
7
>>> K7
7.5
>>> K3=K3+3
>>> K3=K3+K5
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    K3=K3+K5
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> K3=K3+int(K5)
>>> K3
15
>>> 5+3
8
>>> 5-3
2
>>> 5*3
15
>>> 5/3
1.6666666666666667
>>> 5//3
1
>>> 5%3
2
>>> 5**3
125
>>> "김경복"
'김경복'
>>> "김"+"경복"
'김경복'
>>> "김경"+"복"
'김경복'
>>> "김"+"경"+"복"
'김경복'
>>> a=5
>>> b=3
>>> a+b
8
>>> 성+"김"
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    성+"김"
NameError: name '성' is not defined
>>> 성="김"
>>> 이름="경복"
>>> 성+이름
'김경복'
>>> 이름="경황"
>>> 성+이름
'김경황'
