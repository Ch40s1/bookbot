def main():
    # Get the text from the book
    book_path = "books/frankenstein.txt"
    # book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # Count the number of words in the book
    num_words = get_num_words(text)
    # Print the number of words
    print(f"{num_words} words found in the document")

# get_num_words function
def get_num_words(text):
    # Split the text into words
    words = text.split()
    # Return the number of words
    return len(words)

# get_book_text function
def get_book_text(path):
    # Open the file and read the text
    with open(path) as f:
        # Return the text
        return f.read()


main()
