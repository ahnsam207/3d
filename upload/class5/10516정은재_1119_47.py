Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
stu = {"학번":2025,"소속":"AI","이름":"김경복"}
stu ["이름"]
'김경복'
print(''.map(stu))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(''.map(stu))
AttributeError: 'str' object has no attribute 'map'
print(''.join(map(stu)))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(''.join(map(stu)))
TypeError: map() must have at least two arguments.
print(''.join(stu))
학번소속이름
print(''.join(str,stu))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(''.join(str,stu))
TypeError: str.join() takes exactly one argument (2 given)
print
<built-in function print>
print\


       
<built-in function print>


p
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    p
NameError: name 'p' is not defined

print(''.join(stu))
학번소속이름
student
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    student
NameError: name 'student' is not defined
stu
{'학번': 2025, '소속': 'AI', '이름': '김경복'}
>>> stu = {"학번":2025,"소속":"AI","이름":"김경복"}
>>> stu = {"학번":2025,"소속":"AI","이름":"김경복"}
>>> 
>>> \
... 
...   stu
...   
SyntaxError: unexpected indent
>>> stu['학년'] = 1
>>> stu
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 1}
>>> stu['학년'] = 2
>>> stu
{'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
>>> del stu['소속']
>>> stu
{'학번': 2025, '이름': '김경복', '학년': 2}
>>> f"내이름은 {stu['이름']}, 학년은 {stu['학년']}학년 입니다."
'내이름은 김경복, 학년은 2학년 입니다.'
