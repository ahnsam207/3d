Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5+3
8
5-3
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
>>> "김"+경복
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    "김"+경복
NameError: name '경복' is not defined
>>> 김" + 경복
SyntaxError: unterminated string literal (detected at line 1)
>>> "김" + "경복"
'김경복'
>>> "김경" + "복"
'김경복'
>>> "김" + "경" + "복"
'김경복'
>>> a = 5
>>> b = 3
>>> a + b
8
>>> 성 = "김"
>>> 이름 = "경복"
>>> 성 + 이름
'김경복'
>>> 병 = 김
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    병 = 김
NameError: name '김' is not defined
>>> 병 = "김"
