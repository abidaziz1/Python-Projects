import re

def fetch_unique_sorted_words(filename):
    """Fetch unique sorted words from a given text file.

    Args:
        filename (str): The path to the text file.

    Returns:
        list: A sorted list of unique words (case-insensitive).
    """
    try:
        with open(filename, "r") as f:
            words = []
            for line in f:
                # Extract words from the line, ignoring case
                words.extend(re.findall(r"\w+", line.lower()))
                
        # Count occurrences of each word using a dictionary
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # Filter out words that occur more than once
        unique_words = [word for word, count in word_count.items() if count == 1]
        
        return sorted(unique_words)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

if __name__ == "__main__":
    # filename = input("Enter the file name: ")
    filename = "text_file.txt"
    
    unique_sorted_words = fetch_unique_sorted_words(filename)
    
    if unique_sorted_words:
        print("Unique sorted words:", unique_sorted_words)
