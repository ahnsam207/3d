Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5=+3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
5-3
2
5/3
1.6666666666666667
>>> 5//3
1
>>> 5%3
2
>>> 5%%3
SyntaxError: invalid syntax
>>> 5**3
125
>>> 김경+복
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    김경+복
NameError: name '김경' is not defined
>>> "김경"+"복"
'김경복'
>>> a=10
>>> b+7
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b+7
NameError: name 'b' is not defined
>>> b=7
>>> a+b
17
>>> a_b
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a_b
NameError: name 'a_b' is not defined
>>> a-b
3
>>> a*b
70
>>> tjd="김"
>>> 성="김"
>>> 이름="경복"
>>> name=성+이름
>>> name
'김경복'
