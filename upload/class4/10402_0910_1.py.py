Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
type(7)
<class 'int'>
type(7.5)
<class 'float'>
type('경복')
<class 'str'>
type("7.5")
<class 'str'>
a = int(input())

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: ''













































5+'7'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    5+'7'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 3**8
6561
>>> 35211**57
14476596852341413284628243467823127081729924798850928229031189425544442392318422772267101899466034752533704363568613552454650602025612393404488317573517450197136351996543470226903726773573684520704679349451125597030129542567384957978754290969337991531261150571
>>> float("7,5")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float("7,5")
ValueError: could not convert string to float: '7,5'
>>> float('7.5')+5
12.5
>>> 
>>> int(float(10.7))
10
>>> int(10.7)
10
>>> int(float('3.5')*3)+5
15
>>> 0b0101
5
>>> 0b1010
10
>>> 0b0111010111010111
30167
>>> 0b11010
26
>>> 0o4475
2365
>>> 0xA1
161
>>> 0xa1
161
>>> str(int(int(float('3.5'))*3.5))
'10'
