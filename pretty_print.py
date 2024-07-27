'''
The pprint.pformat function in Python is used to create a neatly formatted string representation of complex data structures.
When debugging code, especially when dealing with complex data structures, it can be very helpful to print the data in a readable format to understand its structure and content.

'''
import pprint

# A complex nested data structure
data = {
    'name': 'John Doe',
    'age': 30,
    'children': [
        {'name': 'Jane Doe', 'age': 10},
        {'name': 'Jack Doe', 'age': 8}
    ],
    'pets': [
        {'type': 'dog', 'name': 'Fido'},
        {'type': 'cat', 'name': 'Whiskers'}
    ],
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'zip': '12345'
    }
}

# Pretty-print the data structure to a string
formatted_data = pprint.pformat(data)

# Print the formatted string
print(formatted_data)


import logging

logging.basicConfig(level=logging.INFO)
data = {'name': 'John Doe', 'age': 30, 'children': [{'name': 'Jane Doe', 'age': 10}, {'name': 'Jack Doe', 'age': 8}], 'pets': [{'type': 'dog', 'name': 'Fido'}, {'type': 'cat', 'name': 'Whiskers'}], 'address': {'street': '123 Main St', 'city': 'Anytown', 'zip': '12345'}}
logging.info("User data:\n%s", pprint.pformat(data))
