Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> input()
5
'5'
>>> input(input())
5
5
''
>>> days = input()
5
>>> days
'5'
>>> days = input()
5
>>> days = input()

>>> days = imput
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    days = imput
NameError: name 'imput' is not defined. Did you mean: 'input'?
>>> days = input
>>> days = input(" 일수를 입력히세요;'))
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> days = input(' 일수를 입력히세요;'))
SyntaxError: unmatched ')'
>>> days = input(' 일수를 입력히세요;')
 일수를 입력히세요;5
>>>  days
...  
SyntaxError: unexpected indent
>>> days
'5'
