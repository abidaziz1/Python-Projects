# Reading ZIP files
>>> import zipfile, os
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()

'''
The command at u calculates how efficiently example.zip is compressed
by dividing the original file size by the compressed file size and prints this
information using a string formatted with %s.
'''


# Extracting from ZIP Files
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.extractall()
>>> exampleZip.close()

>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
'''
The extract() method for ZipFile objects will extract a single file from
the ZIP file.
'''


# Creating and Adding to ZIP Files
>>> newZip = zipfile.ZipFile('new.zip', 'a')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) # This specifies the deflate compression algorithm, which works well on all types of data
>>> newZip.close()
'''
This code will create a new ZIP file named new.zip that has the com-
pressed contents of spam.txt.
Keep in mind that, just as with writing to files, write mode will erase
all existing contents of a ZIP file. '''