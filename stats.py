def get_num_words(text):
    words = text.split()
    words_count = len(words)
    return words_count

def get_characters_count(text):
    chars = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in chars:
            chars[lowercase_char] += 1
        else:
            chars[lowercase_char] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list