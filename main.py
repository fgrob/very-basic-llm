from PyPDF2 import PdfReader
import random
import config  # Import configuration

# Define the path to the folder containing the PDF
PDF_FOLDER = "pdfs/"
PDF_PATH = PDF_FOLDER + config.PDF_FILE_NAME  # Full path to the PDF file

# Read the PDF file
reader = PdfReader(PDF_PATH)
successor_map = {}  # Dictionary to store word pairs and their successors
window = []  # Sliding window to process text

# Build the successor map
for page in reader.pages:
    text = page.extract_text()  # Extract text from the page
    for line in text.splitlines():  # Split text into lines
        for word in line.split():  # Split each line into words
            # Clean and normalize the word (remove punctuation, convert to lowercase)
            clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
            window.append(clean_word)  # Add word to the sliding window

            # If the window has 3 words, update the successor map
            if len(window) == 3:
                key = (window[0], window[1])  # Key: first two words
                value = window[2]  # Successor: third word
                successor_map.setdefault(key, []).append(value)  # Add successor
                window.pop(0)  # Slide the window

# Select random starting words
word1, word2 = random.choice(list(successor_map.keys()))  # Randomly pick a word pair

# Generate text
for _ in range(config.WORDS_TO_GENERATE):  # Generate the specified number of words
    print(word1, end=" ")  # Print the current word
    word3 = random.choice(successor_map[(word1, word2)])  # Pick a random successor
    word1, word2 = word2, word3  # Move the window forward

# Print the last word
print(word2)
