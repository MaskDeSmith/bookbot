def main():
    book_path = "books/frankenstein.txt"
    full_text = get_book_text(book_path)
    word_count = get_word_count(full_text)
    print(f"{word_count} is the word count")
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
def get_word_count(full_text):
    words = full_text.split()
    return len(words)
main()