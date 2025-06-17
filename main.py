def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
    return file_contents

def count_word(book_text):
    word = book_text.split()
    num_word = len(word)
    return num_word

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_word = count_word(book_text)
    print(f"{num_word} words found in the document")
main()



    