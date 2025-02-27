from stats import get_num_words
from stats import sort_by_count


def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()

    words = file_contents.split()

    print(f"--- Begin report of {file} ---")
    print("---------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("-------- Character Count --------")
    dict = get_num_words(file_contents)
    sorted_dict = sort_by_count(dict)
    for item in sorted_dict:
        print(f"{item['char']}: {item['count']}")


main()
