# Simple LLM-Based Text Generator

This is a simple Python program that simulates the basic functionality of a Large Language Model (LLM). It reads a PDF file, creates a successor map based on word pairs, and generates a sequence of text by randomly selecting successor words.

## How It Works
1. **Read a PDF file:** The program extracts text from a PDF file located in a folder called `pdfs/`.
2. **Build a successor map:** It creates a dictionary where keys are word pairs, and values are the words that follow them in the text.
3. **Generate text:** Starting from a random pair of words, it generates a sequence of words based on the successor map.

## Prerequisites
- Python 3.8 or higher
- Required libraries listed in `requirements.txt`

## Setup Instructions
1. **Install dependencies:** Use the `requirements.txt` file to install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your PDF file:** Create a folder named `pdfs/` in the root of the project. Place your PDF file inside the `pdfs/` folder. Update the file name in `config.py`:
   ```python
   PDF_FILE_NAME = "your_file_name.pdf"
   ```

3. **Run the program:** Execute the Python program:
   ```bash
   python main.py
   ```
