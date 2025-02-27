import sys
from stats import get_num_words
from stats import sort_by_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
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
