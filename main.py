def main():
    
    book_path = "books/frankenstein.txt"
    full_text = get_book_text(book_path)
    word_count = get_word_count(full_text)
    final_character_count = get_character_count(full_text)
    print(f"{final_character_count} each characters amount")
    print(f"{word_count} is the word count")
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_count(full_text):
    words = full_text.split()
    return len(words)

def get_character_count(full_text):
    lower_string = full_text.lower()
    character_count = {}
    for character in lower_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
            
            
main()