'''
The requests module lets you easily download files from the Web without 
having to worry about complicated issues such as network errors, connec
tion problems, and data compression.
'''
import requests

# # Example of a GET request used to retrieve information from the given server using a given URL.
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.status_code)  # Status code
# print(response.json())  # JSON response content

# The POST method is used to send data to the server to create/update a resource.
url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, json=payload, headers=headers) # Use the requests.post method to send the POST request. The json parameter automatically converts the payload dictionary to a JSON string. The headers parameter is optional.
print(f'Status Code: {response.status_code}') # The status code indicates the result of the request. For a successful POST request, you might expect a status code of 201 (Created).
print(f'Response JSON: {response.json()}') # The response from the server is typically in JSON format. The response.json() method parses the JSON response into a Python dictionary.

# Example of a DELETE request used to delete a resource from the server.
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)  # Status code

# Example of a HEAD request used to retrieve the headers for a resource.
response = requests.head('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)  # Status code
print(response.headers)  # Headers

# The OPTIONS method is used to describe the communication options for the target resource.
response = requests.options('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)  # Status code
print(response.headers)  # Headers

# The PATCH method is used to apply partial modifications to a resource.
payload = {'title': 'foo updated'}
response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=payload)
print(response.status_code)  # Status code
print(response.json())  # JSON response content


# Handling Request Exceptions
from requests.exceptions import HTTPError
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')


# Adding Custom Headers
# Example of a GET request with custom headers
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
print(response.status_code)  # Status code
print(response.json())  # JSON response content


# Sending Data with URL Parameters
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(response.status_code)  # Status code
print(response.json())  # JSON response content


# Uploading Files
files = {'file': open('test.txt', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
file['file'].close()
print(response.status_code)  # Status code
print(response.json())  # JSON response content


# A Session object in the requests module allows you to persist certain parameters across multiple requests. This includes headers, cookies, and connection pooling. This can be useful for maintaining a logged-in state, reusing TCP connections, or sharing common headers across requests.
session = requests.Session()
# Set common headers
session.headers.update({'Authorization': 'Bearer YOUR_ACCESS_TOKEN'})
# Define the URL of the API endpoints
url_get = 'https://jsonplaceholder.typicode.com/posts'
url_post = 'https://jsonplaceholder.typicode.com/posts'
# Make a GET request using the session
response_get = session.get(url_get)
print(f'GET Status Code: {response_get.status_code}')
print(f'GET Response JSON: {response_get.json()}')
# Define the data to be sent in the body of the POST request
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
# Make a POST request using the session
response_post = session.post(url_post, json=payload)
print(f'POST Status Code: {response_post.status_code}')
print(f'POST Response JSON: {response_post.json()}')