from urllib.request import urlopen
import time
import urllib.error


def get_load_time(url):
    """This function takes a user-defined url as input
    and returns the time taken to load that url in seconds.

    Args:
        url (string): The user-defined url.

    Returns:
        time_to_load (float): The time taken to load the website in seconds, or None if an error occurs.
    """
    if not url.startswith(("http://", "https://")):  # Check if the URL has a protocol
        url = "https://" + url  # Default to https if no protocol is specified

    try:
        start_time = time.time()  # Time stamp before the reading of the url starts
        with urlopen(url) as open_this_url:  # Open the URL using 'with' for better resource handling
            open_this_url.read()  # Reading the user-defined URL
        end_time = time.time()  # Time stamp after the reading of the url
        time_to_load = end_time - start_time
        return time_to_load
    except urllib.error.URLError as e:
        print(f"Error: Unable to load the URL. {e.reason}")
        return None


if __name__ == '__main__':
    url = input("Enter the URL whose loading time you want to check: ")
    load_time = get_load_time(url)
    if load_time is not None:
        print(f"\nThe time taken to load {url} is {load_time:.2f} seconds.")
