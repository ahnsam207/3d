Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
k3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    k3
NameError: name 'k3' is not defined
k3=7
k3
7
k5="5"
k5
'5'
type(k3)
<class 'int'>
type(k5)
<class 'str'>
7=
SyntaxError: cannot assign to literal

k7=7.5
k7
7.5
type(k7)
<class 'float'>
k3
7
k5
'5'
k7
7.5
k3=k3+3
k3
10
k3= k3+ int(k5)
k3
15
k5= k5+ str(k7)
k5
'57.5'
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
>>> a
5
>>> v
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> b
3
>>> a+b
8
>>> 성="김"
>>> 이름="경복"
>>> 성+이름
'김경복'
