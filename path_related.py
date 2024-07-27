# Backslash on Windows and Forward Slash on OS X and Linux
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'

'''
If I had called this function on OS X or Linux, the string would have been 'usr/bin/spam'.
'''

>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
'''C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx'''


>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'

# Absolute vs. Relative Paths
"""•	An absolute path, which always begins with the root folder
•	A relative path, which is relative to the program’s current working 
directory. A single period (“dot”) 
for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) 
means “the parent folder.”"""


# Creating New Folders with os.makedirs()
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')


>>> os.path.abspath('.')
'C:\\Python34'
>>> os.path.abspath('.\\Scripts')
'C:\\Python34\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True


>>> os.path.relpath('C:\\Windows', 'C:\\')
 'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
 '..\\..\\Windows'
>>> os.getcwd()
 'C:\\Python34'


C:\Windows\System32\calc.exe
C:\Windows\System32->Dir name
calc.exe->Base name

>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path)
 'calc.exe'
>>> os.path.dirname(path)
 'C:\\Windows\\System32'


'''
If you need a path’s dir name and base name together, you can just call 
os.path.split() to get a tuple value with these two strings
'''
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')


>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('C:\\Windows\\System32', 'calc.exe')  # Same Result


>>> calcFilePath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']


>>> '/usr/bin'.split(os.path.sep)
['', 'usr', 'bin']


>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
776192
>>> os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',--snip-
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']


>>> os.path.exists('C:\\Windows')
 True
>>> os.path.exists('C:\\some_made_up_folder')
 False
>>> os.path.isdir('C:\\Windows\\System32')
 True
>>> os.path.isfile('C:\\Windows\\System32')
 False
>>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
 False
>>> os.path.isfile('C:\\Windows\\System32\\calc.exe')
 True


