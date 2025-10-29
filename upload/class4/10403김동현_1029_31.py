Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
lst = list()
lst
[]
lst.appned(90)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    lst.appned(90)
AttributeError: 'list' object has no attribute 'appned'. Did you mean: 'append'?
>>> lst.append(90)
>>> lst
[90]
>>> lst.append(85)
>>> lst
[90, 85]
>>> lst.sort()
>>> lst
[85, 90]
>>> lst.sort(97)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    lst.sort(97)
TypeError: sort() takes no positional arguments
>>> lst.reverse()
>>> lst
[90, 85]
>>> lst.index(90)
0
>>> lst.count(90)
1
>>> lst.pop()
85
>>> lst
[90]
