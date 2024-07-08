from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import os

def print_banner():
    print(r"""
     _____        _   __    ____              _      _
    | ____|__  __(_) / _|  / ___| _ __  __ _ | |__  | |__    ___  _ __
    |  _|  \ \/ /| || |_  | |  _ | '__|/ _` || '_ \ | '_ \  / _ \| '__|
    | |___  >  < | ||  _| | |_| || |  | (_| || |_) || |_) ||  __/| |
    |_____|/_/\_\|_||_|    \____||_|   \__,_||_.__/ |_.__/  \___||_|

    # Extract EXIF data from picture
    # Coded By Abid Aziz
    """)

def extract_hachoir_metadata(photo):
    """Extract metadata using hachoir"""
    print("\nExtracting metadata using hachoir...\n")
    try:
        if not os.path.isfile(photo):
            raise FileNotFoundError(f"File not found: {photo}")

        parser = createParser(photo)
        if not parser:
            raise FileNotFoundError(f"File not found: {photo}")

        metadata = extractMetadata(parser)
        if not metadata:
            raise ValueError("No metadata found")

        for line in metadata.exportPlaintext():
            print(line)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print_banner()
    photo = input("\nPhoto Name (with full path): ").strip()  # Prompt the user to input the photo name with the full path
    # Remove quotes from the input if present
    if photo.startswith('"') and photo.endswith('"'):
        photo = photo[1:-1]
    extract_hachoir_metadata(photo)  # Extract metadata using hachoir

if __name__ == "__main__":
    main()
