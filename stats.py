def get_num_words(string):
    chars = {}
    # Create a list of characters a-z
    # a in ascii decimal code = 97. z = 122
    for i in range(97, 123):
        chars.update({chr(i): 0})

    for char in list(string.lower()):
        if char in chars.keys():
            chars[char] += 1

    return chars


def sort_on(dict):
    return dict["count"]


def sort_by_count(dict):
    new_list = []
    for char, count in dict.items():
        new_list.append({"char": char, "count": count})
        new_list.sort(reverse=True, key=sort_on)
    return new_list
