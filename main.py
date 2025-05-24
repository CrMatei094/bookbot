import sys
from stats import ( 
    get_num_words, 
    get_characters_count, 
    chars_dict_to_sorted_list,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    words_string = "words found in the document"
    text = get_book_text(book_path)
    chars_count = get_characters_count(text)
    num_words = get_num_words(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_count)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()