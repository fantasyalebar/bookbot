import sys
from stats import get_num_words, count_characters, get_chars_for_report, print_report


def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_word = get_num_words(book_text)
    letter_word = count_characters(book_text)
    char_list = get_chars_for_report(letter_word)
    print_report(num_word, char_list)
main()
