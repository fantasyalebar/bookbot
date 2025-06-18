from stats import get_num_words
from stats import count_characters

def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_word = get_num_words(book_text)
    print(f"{num_word} words found in the document")
    letter_word = count_characters(book_text)
    print(letter_word)
main()

