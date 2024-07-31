import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


import requests
from bs4 import BeautifulSoup

# Function to get all links from a webpage
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return links

# URL of the webpage
url = 'https://example.com'
links = get_links(url)

# Open each link in a new browser tab
for link in links:
    webbrowser.open_new_tab(link)




# List of social network URLs
social_networks = [
    'https://www.facebook.com',
    'https://www.twitter.com',
    'https://www.linkedin.com',
    'https://www.instagram.com'
]

# Open each social network site in a new browser tab
for site in social_networks:
    webbrowser.open_new_tab(site)




# Specify the location
location = 'New York, NY'

# URL for the weather information (using a placeholder for the location)
weather_url = f'https://www.weather.com/weather/today/l/{location}'

# Open the browser to the weather URL
webbrowser.open(weather_url)
