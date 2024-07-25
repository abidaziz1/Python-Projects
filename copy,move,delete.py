import shutil,os
os.chdir('E:\\')
shutil.copy('D:\Patrick+Engebretson+The+Basics+of+Hacking+and+Penetration+Testing,+Second+Edition+(2013)[1].pdf', 'E:\Courses\PDFs\pentesting.pdf')

'''
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') # copies the file at C:\eggs.txt to the folder C:\delicious but gives
the copied file the name eggs2.txt.

>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
shutil.copytree() call creates a new folder named bacon_backup with
the same content as the original bacon folder.
'''

# Moving and Renaming Files and Folders
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'''says, “Move C:\bacon.txt into the folder C:\eggs, and while
you’re at it, rename that bacon.txt file to new_bacon.txt.”'''

# Permanently Deleting Files and Folders
'''
• Calling os.unlink(path) will delete the file at path.
• Calling os.rmdir(path) will delete the folder at path. This folder must be
empty of any files or folders.
• Calling shutil.rmtree(path) will remove the folder at path, and all files
and folders it contains will also be deleted.
'''
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)    # first see if there is any important files with that extension, then delete it
        print(filename)

# Safe Deletes with the send2trash Module
import send2trash
baconFile = with open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
'''
Using send2trash is much safer than Python’s regular delete functions,
because it will send folders and files to your computer’s trash or recycle bin
instead of permanently deleting them. If a bug in your program deletes
something with send2trash you didn’t intend to delete, you can later restore
it from the recycle bin. it will not free up disk space like permanently deleting
them does.
'''