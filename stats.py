def sort_on(items):
    return items["num"]


def dict_creator(dict: dict[str, int]):
    dict_list = []
    for item in dict:
        dict_list.append({"char": item, "num": dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def words_count(text: str):
    words = text.split()
    return len(words)


def char_counts(text: str):
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] = chars_dict[char] + 1
        else:
            chars_dict[char] = 1
    return chars_dict
