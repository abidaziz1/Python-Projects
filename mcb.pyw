#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

# Open the shelf file to store the clipboard contents
mcbShelf = shelve.open('mcb')

# Save clipboard content to a keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # If the first command line argument is 'save', the second argument is the keyword
    # The current clipboard content is saved to the shelf file under this keyword
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# List keywords and load content
elif len(sys.argv) == 2:
    # If there's only one command line argument, it's either 'list' or a keyword
    if sys.argv[1].lower() == 'list':
        # If the argument is 'list', copy the list of all keywords to the clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # If the argument is a keyword, copy the corresponding content to the clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])

# Close the shelf file
mcbShelf.close()
