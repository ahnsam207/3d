Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> type(7)
<class 'int'>
>>> type(7.5)
<class 'float'>
>>> type('경복')
<class 'str'>
>>> type(7.5)
<class 'float'>
>>> type('7.5')
<class 'str'>
>>> 5 + "7"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    5 + "7"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 
>>> 5 + int("7")
12
>>> "7.5"
'7.5'
>>> float("7.5")
7.5
>>> 5 + float("7.5")
12.5
>>> int(10.7)
10
>>> str(니얼굴)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str(니얼굴)
NameError: name '니얼굴' is not defined
>>> int(니얼굴)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int(니얼굴)
NameError: name '니얼굴' is not defined
>>> int(float('3.5')*3) + 5
15
>>> 0b1010
10
>>> ob1100101
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ob1100101
NameError: name 'ob1100101' is not defined
>>> ob0101
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ob0101
NameError: name 'ob0101' is not defined
>>> 0b1000101110101011111
286047
>>> 0b1010101011101010101101101010010010110001010101010101101010110001010010101110011001101010110101001010101010110100010100110100101000101111001101000101101010101010101010101110100100101010100101010
8381737906846662386396010079087443284133052076333280154922
>>> 0xa1
161
>>> 0xA1
161
>>> 161 0xa1
SyntaxError: invalid syntax
>>> str(int(int(float('3.5'))*3.5))
'10'
