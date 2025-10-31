Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
ist = []
lst
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    lst
NameError: name 'lst' is not defined. Did you mean: 'ist'?
lst = []
lst
[]
lst1= list()
lst.append(90)
lst
[90]
lst.apppend(85)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lst.apppend(85)
AttributeError: 'list' object has no attribute 'apppend'. Did you mean: 'append'?
lst.apppend(85)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    lst.apppend(85)
AttributeError: 'list' object has no attribute 'apppend'. Did you mean: 'append'?
lst.append(85)
lst
[90, 85]
lst.append(97)
lst
[90, 85, 97]
lst.soer()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    lst.soer()
AttributeError: 'list' object has no attribute 'soer'
lst.sort
<built-in method sort of list object at 0x000001EDFE6E5C80>
lst.sort()
lst
[85, 90, 97]
lst.reverse()
lst
[97, 90, 85]
lst.index()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    lst.index()
TypeError: index expected at least 1 argument, got 0
lst.index()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lst.index()
TypeError: index expected at least 1 argument, got 0
lst.index(90)
1
lst.count(90)
1
lst.append(90)
lst.count(90)
2
>>> lst
[97, 90, 85, 90]
>>> 
>>> lst1.append("유재석")
>>> lst
[97, 90, 85, 90]
>>> lst1
['유재석']
>>> ls1.append("박명수")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ls1.append("박명수")
NameError: name 'ls1' is not defined. Did you mean: 'lst'?
>>> lst1.append("박명수")
>>> lst1
['유재석', '박명수']
>>> lst1.append("하하")
>>> ㅣㄴㅅ1
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ㅣㄴㅅ1
NameError: name 'ᅵᄂᄉ1' is not defined
>>> lst1
['유재석', '박명수', '하하']
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
>>> lst1.pop()
'박명수'
>>> lst1
['하하', '유재석']
