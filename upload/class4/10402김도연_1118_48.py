Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = {}
>>> c['빨강'] = 'Red'
>>> c['파랑'] = 'Blue'
>>> c['노랑'] = 'Yellow'
>>> c['초록'] = 'Green'
>>> c['주황'] = 'Orange'
>>> c['남색'] = 'Indigo'
>>> c['분홍'] = 'pink'
>>> c['흰색'] = 'White'
>>> c['검정'] = 'Black'
>>> c['분홍'] = 'Pink'
>>> for i in color:
...     print('%s는 %s입니다.' %(i,color[i]))
... 
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for i in color:
NameError: name 'color' is not defined
>>> for i in c:
...     print('%s는 %s입니다.' %(i,c[i]))
... 
빨강는 Red입니다.
파랑는 Blue입니다.
노랑는 Yellow입니다.
초록는 Green입니다.
주황는 Orange입니다.
남색는 Indigo입니다.
분홍는 Pink입니다.
흰색는 White입니다.
검정는 Black입니다.
