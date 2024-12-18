def main():
    
    book_path = "books/frankenstein.txt"
    full_text = get_book_text(book_path)
    word_count = get_word_count(full_text)
    final_character_count = get_character_count(full_text)
    sorted_character_count = get_sorted_character_count(final_character_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in sorted_character_count:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

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

def sort_on(d):
    return d["num"]

def get_sorted_character_count(final_character_count):
    sorted_list = []
    for value in final_character_count:
        sorted_list.append({"char": value, "num": final_character_count[value]})            
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
