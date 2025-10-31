Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

lst = []
lst
[]
lst = list()
lst1 = list()
lst.append(90)
lst
[90]
lst.appen(85)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lst.appen(85)
AttributeError: 'list' object has no attribute 'appen'. Did you mean: 'append'?
le
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    le
NameError: name 'le' is not defined. Did you mean: 'len'?
=lst.append(85)
lst.append(85)
lst
[90, 85, 85]
lst.remove(85)
lst
[90, 85]
lst.append(97)
lst
[90, 85, 97]
lst.sort()
lst
[85, 90, 97]
lst.index(90)
1
ist.count(90)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ist.count(90)
NameError: name 'ist' is not defined. Did you mean: 'lst'?
lst.count(90)
1
lst.append(90)
lst
[85, 90, 97, 90]
lst.count(90)
2
lst1.append("유재석")
lst1
['유재석']
lst1.append("박명수")
lst1
['유재석', '박명수']

lst1.append("하하")
lst1
['유재석', '박명수', '하하']
lst1.reverse()
lst1
['하하', '박명수', '유재석']
lst1,index("유재석")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lst1,index("유재석")
NameError: name 'index' is not defined
lst.index(:"유재석")
SyntaxError: invalid syntax
lst.index("유재석")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    lst.index("유재석")
ValueError: '유재석' is not in list
lst1.index("유재석")
2














... 
>>> 

>>> 

... 
>>> 

>>>  ㄴ
...  
SyntaxError: unexpected indent
>>> lse1.count('박명수')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lse1.count('박명수')
NameError: name 'lse1' is not defined. Did you mean: 'lst1'?
>>> 
>>> lst1.count('박명수')
1
>>> lst1.pop()
'유재석'
>>> lst1
['하하', '박명수']
