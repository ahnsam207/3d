Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
lst = []
lst
[]
lst1 = ;ist()
SyntaxError: invalid syntax
lst1 = list()
lst.append(90)
lst
[90]
lst.append(85)
lst
[90, 85]
lst.append(97)
lst
[90, 85, 97]
lst.sort()
lst
[85, 90, 97]
lst.reverse
<built-in method reverse of list object at 0x000001A5423260C0>
lst.reverse()
lst
[97, 90, 85]
lst.index(90)
1
lst.index(85)
2
lst.count(90)
1
lst.count(97,90,85)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    lst.count(97,90,85)
TypeError: list.count() takes exactly one argument (3 given)
>>> lst.appand(90)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    lst.appand(90)
AttributeError: 'list' object has no attribute 'appand'. Did you mean: 'append'?
>>> lst.append(90)
>>> lst
[97, 90, 85, 90]
>>> lst.count(90)
2
>>> lst1.append("유재석")
>>> lst1
['유재석']
\
>>> lst1.append("박명수")
>>> lst1
['유재석', '박명수']
>>> lst1.append("하하")
>>> lst1
['유재석', '박명수', '하하']
>>> lst1,sort()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lst1,sort()
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> lst1.sort()
>>> lst1
['박명수', '유재석', '하하']
>>> lst1.reverse()
>>> lst1
['하하', '유재석', '박명수']
>>> lst1.index("유재석")
1
>>> lst1.count("하하")
1
>>> lst1.pop()
'박명수'
>>> lst1
['하하', '유재석']
