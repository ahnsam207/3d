Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a2 = 1
>>> 5a = a2 * 2
SyntaxError: invalid decimal literal
>>> 5a = a2 + 2
SyntaxError: invalid decimal literal
>>> 1a = a2 + 2
SyntaxError: invalid decimal literal
>>> a1 = a2 + 2
>>> print(a1)
3
>>> 3
3
>>> d1 = 3
>>> print(d1)
3
>>> d5 = str
>>> d2 = int
>>> print(d2(1) + 2))
SyntaxError: unmatched ')'
>>> print(d2(1) + 1)
2
>>> printt
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    printt
NameError: name 'printt' is not defined. Did you mean: 'print'?
>>> 
>>> print(d2(10) + a2)
11
>>> 5a = a2 + 2
SyntaxError: invalid decimal literal
>>> a2
1
>>> d2
<class 'int'>
>>> d2
<class 'int'>
>>> 5 // 9
0
>>> 5 // 123
0
>>> 12 // 6
2
>>> 5 % 3
2
>>> 5 % 12
5
>>> 5 ** 9
1953125
>>> "김" + "경" 1
SyntaxError: invalid syntax
>>> "김" + "경"
'김경'
>>> "4" * 3
'444'
>>> "4" * 4
'4444'
>>>                                      "4"
...                                      
SyntaxError: unexpected indent
>>> "4" * 12
'444444444444'
>>> "4" * 125
'44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444'
>>> a = 12
>>> b = int
>>> print(a + b(1))
13
>>> print(a + b(100))
112
