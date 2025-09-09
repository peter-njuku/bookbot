def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_dict(text):
    char_count = {}
    for chars in text:
        lowered_chars = chars.lower()
        if lowered_chars in char_count:
            char_count[lowered_chars] += 1
        else:
            char_count[lowered_chars] = 1
    return char_count

def sort_d(d):
    return d["num"]

def chars_dict_sorted_to_list(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]} )

    return sorted_list
