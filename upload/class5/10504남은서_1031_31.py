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
lst.reverse()
>>> lst
[97, 85, 90]
>>> lst.index(90)
2
>>> lst.count(90)
1
>>> lst.append(90)
>>> lst
[97, 85, 90, 90]
>>> lst.count(90)
2
>>> lst1.append("유재석")
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
>>> lst1.index("유재석")
1
>>> lse1.count('박명수')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    lse1.count('박명수')
NameError: name 'lse1' is not defined. Did you mean: 'lst1'?
>>> lst1.count("박명수")
1
>>> lst1.pop()
'박명수'
>>> lst1
['하하', '유재석']
