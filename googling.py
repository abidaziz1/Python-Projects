import requests # for downloading web pages.
import sys
import webbrowser # for opening web pages in the browser.
import bs4 # for parsing HTML.
import urllib.parse

print('Googling...')  # Display text while downloading the Google page

# Get the search keywords from the command line arguments
search_keywords = ' '.join(sys.argv[1:]) # gets the search terms.

# URL-encode the search query
search_keywords = urllib.parse.quote(search_keywords)

# Set a User-Agent header
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    # Send the request
    res = requests.get('http://google.com/search?q=' + search_keywords, headers=headers)
    res.raise_for_status()
except requests.RequestException as e:
    print(f"Request error: {e}")
    sys.exit(1)

try:
    # Parse the HTML
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
except Exception as e:
    print(f"Parsing error: {e}")
    sys.exit(1)

# Retrieve top search result links
linkElems = soup.select('.r a')

# Open a browser tab for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    href = linkElems[i].get('href')
    if href.startswith('/url?q='):
        webbrowser.open('http://google.com' + href)


"""
BEGIN
    IMPORT necessary modules: requests, sys, webbrowser, bs4
    
    PRINT "Googling..."
    
    // Step 1: Get search keywords from command line arguments
    search_keywords = JOIN(sys.argv[1:])
    
    // Step 2: Send a search request to Google
    search_url = 'http://google.com/search?q=' + search_keywords
    response = requests.get(search_url)
    IF response.raise_for_status() THROWS error THEN
        HANDLE error
    END IF
    
    // Step 3: Parse the search results page
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    // Step 4: Extract search result links
    link_elements = soup.select('.r a')
    
    // Step 5: Open browser tabs for top results
    num_links_to_open = MIN(5, LENGTH(link_elements))
    FOR i FROM 0 TO num_links_to_open - 1 DO
        link = 'http://google.com' + link_elements[i].get('href')
        webbrowser.open(link)
    END FOR
END

"""