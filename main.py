from stats import count_words
import sys


def get_book_content(book_path: str) -> str:
    with open(book_path, "r") as f:
        file_content = f.read()
        return file_content


def count_character(book_content: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}
    
    for text in book_content.split():
        lower_text = text.lower()
        for char in lower_text:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] +=1
                else:
                    char_dict[char] = 1
    return char_dict

def sort_on(char_dict: dict) -> int:
    return char_dict["num"]

def print_report(book_path: str, char_dict: dict, num_word: int) -> None:
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_word} words found in the document")
    char = []

    for letter, num in char_dict.items():
        per_dict = {}
        per_dict["character"] = letter
        per_dict["num"] = num
        char.append(per_dict)

    char.sort(reverse=True, key=sort_on)

    for content in char:
        character = content["character"]
        value = content["num"]
        print(f"{character}: {value}")

    print("--- End report ---")


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_content = get_book_content(book_path)
    num_words = count_words(book_content)
    char_dict = count_character(book_content)
    print_report(book_path, char_dict, num_words)


if __name__ == "__main__":
    main()
