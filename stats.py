
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