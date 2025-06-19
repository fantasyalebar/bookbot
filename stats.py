
def get_num_words(book_text):
    word = book_text.split()
    num_word = len(word)
    return num_word

def count_characters(text):
    # Créer un dictionnaire vide
    char_count = {}
    
    for character in text:
        lower_char = character.lower()
        if lower_char in char_count:
            # Le caractère existe déjà, ajoute 1 à son compte
            char_count[lower_char] = char_count[lower_char] + 1
        else:
            # Le caractère n'existe pas encore, commence à 1
            char_count[lower_char] = 1
    return char_count


def get_chars_for_report(char_counts_dict):
    char_list = [] 
    for char, num in char_counts_dict.items():
        new_character_dict = {"char": char, "num": num}
        char_list.append(new_character_dict)
    return char_list

def sort_on(dict):
    return dict["num"]

def print_report(num_word, char_list):
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        character = char_dict["char"]
        if character.isalpha():
            print(f"{character}: {char_dict['num']}")
    print("============= END ===============")
