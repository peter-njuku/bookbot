from stats import get_num_words, get_char_dict, chars_dict_sorted_to_list

def get_book_text(file_path):
    with open(file_path) as f:
        file = f.read()
    return file

def print_report(book_path, num_words, chars_sorted_list):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}:{item["num"]}")
    print("============= END =============")

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    chars_sorted_list = chars_dict_sorted_to_list(chars_dict)
    print(f"{num_words} words found in the document")
    print_report(book, num_words, chars_sorted_list)

if __name__ == "__main__":
    main()