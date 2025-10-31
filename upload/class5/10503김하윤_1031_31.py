Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
lst=[]
lst
[]
lst1=list()
lst.append(90)
lst
[90]
lst.append(85)
lst
[90, 85]
lst.append(97)
lst
[90, 85, 97]
lst.reverse()
lst
[97, 85, 90]
lsft.index(90)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lsft.index(90)
NameError: name 'lsft' is not defined. Did you mean: 'lst'?
lst.index(90)
2
>>> lst.count(90)
1
>>> lst.append(80)
>>> lst
[97, 85, 90, 80]
>>> lst.count(90)
1
>>> lst1.append("유재석")
>>> lst1
['유재석']
>>> lst.append("박명수")
>>> lst1
['유재석']
>>> lst1.append("박명수")
>>> lst1
['유재석', '박명수']
>>> lst1.append("하하")
>>> lst1
['유재석', '박명수', '하하']
>>> lst1.sort()
>>> lst1
['박명수', '유재석', '하하']
>>> lst1.reverse()
>>> lst1
['하하', '유재석', '박명수']
>>> lst1.inedex("유재석")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lst1.inedex("유재석")
AttributeError: 'list' object has no attribute 'inedex'. Did you mean: 'index'?
>>> lst1.index("유재석")
1
>>> lst1.count('박명수')
1
>>> lst1.pop()
'박명수'
>>> lst1
['하하', '유재석']
