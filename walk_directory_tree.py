import os
for folderName, subfolders, filenames in os.walk('D:\github repository'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')


'''
Since os.walk() returns lists of strings for the subfolder and filename
variables, you can use these lists in their own for loops. Replace the print()
function calls with your own custom code. (Or if you don’t need one or
both of them, remove the for loops.)
'''