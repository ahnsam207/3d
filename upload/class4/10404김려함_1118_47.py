Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> student= {'학번':2025, '소속':'AI', '이름':'김경복'}
... SyntaxError: unexpected indent
... student = {'학번':2025, '소속':'AI', '이름':'김경복'}
... student['이름']
... '김경복'
... student
... {'학번': 2025, '소속': 'AI', '이름': '김경복'}
... student['학년'] = 1
... student
... {'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 1}
... student['학년'] = 2
... student
... {'학번': 2025, '소속': 'AI', '이름': '김경복', '학년': 2}
...  del student['소속']
... student
... {'학번': 2025, '이름': '김경복', '학년': 2}
...  f"내 이름은 {student['이름']}, 학년은 {student['학년']}학년 입니다."
... '내 이름은 김경복, 학년은 2학년 입니다.'
