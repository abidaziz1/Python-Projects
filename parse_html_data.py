import bs4

# Open and read the example HTML file
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

# Select element with id="author"
elems = exampleSoup.select('#author')
print(type(elems))  # Output: <class 'list'>
print(len(elems))   # Output: 1
print(type(elems[0]))  # Output: <class 'bs4.element.Tag'>
print(elems[0].getText())  # Output: 'Al Sweigart'
print(elems[0])  # Output: '<span id="author">Al Sweigart</span>'
print(elems[0].attrs)  # Output: {'id': 'author'}

# Select all <p> elements
pElems = exampleSoup.select('p')
print(pElems[0])  # Output: '<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
print(pElems[0].getText())  # Output: 'Download my Python book from my website.'
print(pElems[1])  # Output: '<p class="slogan">Learn Python the easy way!</p>'
print(pElems[1].getText())  # Output: 'Learn Python the easy way!'
print(pElems[2])  # Output: '<p>By <span id="author">Al Sweigart</span></p>'
print(pElems[2].getText())  # Output: 'By Al Sweigart'

"""
Tag Object Methods:
getText(): Retrieves the text content of the element.
str(): Converts the Tag object to a string, including the starting and closing tags.
attrs: Returns a dictionary of the element’s attributes.
"""

# Getting Data from an Element’s Attributes
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem) # '<span id="author">Al Sweigart</span>'
spanElem.get('id')
 'author'
spanElem.get('some_nonexistent_addr') == None #Returns None if the attribute does not exist.
 True
spanElem.attrs
 {'id': 'author'}