Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
lst = []
lst
[]
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
stl
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    stl
NameError: name 'stl' is not defined. Did you mean: 'str'?
lst
[85, 90, 97]
lst.reverse
<built-in method reverse of list object at 0x000001D5AB2F60C0>
lst
[85, 90, 97]
lst.reverse()
lst
[97, 90, 85]
lst.index(90)
1
lst.count(90)
1
lst.append(90)
>>> lst
[97, 90, 85, 90]
>>> lst.count(90)
2
>>> lst1.append("유재석")
>>> lst1
['유재석']
>>> lst1.append("박명수")
>>> lst
[97, 90, 85, 90]
>>> lst1
['유재석', '박명수']
>>> lst1.append("하하")
>>> lst1.sort()
>>> lst1
['박명수', '유재석', '하하']
>>> lst1.reverse()
>>> lst1
['하하', '유재석', '박명수']
>>> lst1.index("유재석")
1
>>> lst1.count("박명수")
1
>>> lst.pop()
90
>>> lst1.pop()
'박명수'
>>> lst1
['하하', '유재석']
