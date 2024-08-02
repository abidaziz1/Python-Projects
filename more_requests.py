import requests

# Define the URL of the file to be downloaded
url = 'https://example.com/path/to/file'

# Send a GET request to download the file
response = requests.get(url, stream=True)

# Open a local file in write binary mode
with open('downloaded_file', 'wb') as file:
    # Loop over the response content in chunks
    for chunk in response.iter_content(chunk_size=8192): # The iter_content() method allows you to iterate over the response content in chunks. The chunk_size parameter specifies the size of each chunk. This prevents loading the entire file into memory at once.
        # Write the chunk to the file
        if chunk:
            file.write(chunk)

# No need to explicitly call file.close() because the 'with' statement handles it
