Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
lst = []
ist
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ist
NameError: name 'ist' is not defined. Did you mean: 'lst'?
lst
[]
lst1 =list()
lst. append
<built-in method append of list object at 0x0000018EC3425940>
lst. append(90)

lst
[90]
lst. append(85)
lst
[90, 85]
lst. append(97)
lst
[90, 85, 97]
lst.sort()
lst
[85, 90, 97]
lst.reverse()
lst
[97, 90, 85]
lst.index(90)
1
lst.count(90)
1
int.append(90)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int.append(90)
AttributeError: type object 'int' has no attribute 'append'
lst.append
<built-in method append of list object at 0x0000018EC3425940>
lst.append(90)
lst
[97, 90, 85, 90]
lst.count(90)
2
lst1.append("유재석")
ㅣㄴㅅ1
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ㅣㄴㅅ1
NameError: name 'ᅵᄂᄉ1' is not defined
lst1
['유재석']
>>> lst1.append("박명수")
>>> lst1
['유재석', '박명수']
>>> lst1.append("하하")
... lst1
SyntaxError: multiple statements found while compiling a single statement
>>> lst1.append("하하")
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
