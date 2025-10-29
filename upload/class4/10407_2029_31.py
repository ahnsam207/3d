Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> lst
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    lst
NameError: name 'lst' is not defined. Did you mean: 'list'?
>>> lst = list()
>>> lst
[]
>>> lst.append(90)
>>> lst
[90]
>>> lst.append(85)
>>> lst
[90, 85]
>>> lst.append(97)
>>> lst
[90, 85, 97]
>>> lst.sort()
>>> lst
[85, 90, 97]
>>> lst.reverse()
>>> lst
[97, 90, 85]
>>> lst.index(90)
1
>>> lst.count(90)
1
>>> lst.pop()
85
>>> lst
[97, 90]
