Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 5=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 5+3
8
>>> 5-3
2
>>> 5/3
1.6666666666666667
>>> 5*3
15
>>> 5//3
1
>>> 5**3
125
>>> 5%3
2
>>> 5**10000
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    5**10000
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> "김경"+"복"
'김경복'
>>> a=10
>>> b=7
>>> a+b
17
>>> a-b
3
>>> a*b
70
>>> 성 = "김"
>>> 이름="경복"
>>> name=성+이름
>>> name
'김경복'
>>> name*3
'김경복김경복김경복'
