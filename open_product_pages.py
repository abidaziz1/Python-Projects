"""
Algorithm:
Get Search Keywords from Command Line: Read the product search keywords.
Send Search Request: Send an HTTP request to the shopping site's search URL.
Parse Search Results: Use BeautifulSoup to parse the search results page.
Extract Product Links: Use CSS selectors to extract the product links.
Open Product Links in Tabs: Open each product link in a new browser tab.
"""
import requests
import sys
import webbrowser # For opening URLs in the web browser.
import bs4

print('Searching Amazon...')

# Get search keywords from command line arguments (excluding the script name) into a single string representing the search keywords.
search_keywords = ' '.join(sys.argv[1:])
search_url = f'https://www.amazon.com/s?k={search_keywords}'

response = requests.get(search_url) # Sends a GET request to the constructed search URL.
response.raise_for_status() # Raises an error if the request was unsuccessful.

soup = bs4.BeautifulSoup(response.text, 'html.parser') # Creates a BeautifulSoup object to parse the HTML content of the search results page.
link_elements = soup.select('.s-title a')  # Uses a CSS selector to extract links from the search results. The selector .s-title a targets <a> elements within elements with the class s-title.

num_links_to_open = min(5, len(link_elements))
for i in range(num_links_to_open):
    link = 'https://www.amazon.com' + link_elements[i].get('href') # Concatenates the base URL with the relative link obtained from href.
    webbrowser.open(link)
