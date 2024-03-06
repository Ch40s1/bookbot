def main():
    # Get the text from the book
    book_path = "books/frankenstein.txt"
    # book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # Count the number of words in the book
    num_words = get_num_words(text)
    #counts repeating characters in text
    repeating_chracters = get_repeating_char(text)
    #get final string report with word count and all characters and there repeating values
    get_final_report = get_string_report(repeating_chracters)
    # Print the number of words
    print("--- Begin report of books/frankenstine.txt ---")
    print(f"{num_words} words found in the document")
    for item in get_final_report:
       print(f"The \'{item["letter"]}\' character was found {item["count"]} times")
    print("--- End report ---")

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

def get_repeating_char(text):
    new_text = text.lower()
    word_dict = {}
    for character in new_text:
        if character in word_dict:
            word_dict[character] += 1
        else:
            word_dict[character] = 1
    return word_dict

def get_string_report(dict):
    new_dict = {}
    for k, v in dict.items():
        if k.isalpha():
            new_dict[k] = v
    list = []
    for key, value in new_dict.items():
        list.append({"letter":key, "count":value})
    list.sort(reverse=True, key=__sort_on)
    return list

def __sort_on(dict):
    return dict["count"]



main()
