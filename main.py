def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()

    words = file_contents.split()

    print(f"--- Begin report of {file} ---")
    print(f"{len(words)} words found")
    dict = characters(file_contents)
    for char, times in dict.items():
        print(f"The '{char}' character was found {times} times")


def characters(string):
    chars = {}
    # Create a list of characters a-z
    # a in ascii decimal code = 97. z = 122
    for i in range(97, 123):
        chars.update({chr(i): 0})

    for char in list(string.lower()):
        if char in chars.keys():
            chars[char] += 1

    return chars

main()
