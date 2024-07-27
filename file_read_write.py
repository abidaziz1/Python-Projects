>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

#  Reading the Contents of Files
>>> helloContent = helloFile.read()
>>> helloContent
'Hello world!'
'''
create a file named sonnet29.txt in the same directory as hello.txt and write the following text in it:
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
'''
>>> sonnetFile = open('sonnet29.txt')
>>> sonnetFile.readlines()



>>> baconFile = open('bacon.txt', 'w')   
>>> baconFile.write('Hello world!\n')
 13
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a') 
>>> baconFile.write('Bacon is not a vegetable.')
 25
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
 Hello world!
 Bacon is not a vegetable.


>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()

>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile) 
 <class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
 ['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()

>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
 ['cats']
>>> list(shelfFile.values())
 [['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()

