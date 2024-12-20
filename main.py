def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    num_words = count_words(book_content)
    char_dict = count_character(book_content)
    print_report(book_path, char_dict, num_words)

def get_book_content(book_path):
    with open(book_path, "r") as f:
        file_content = f.read()
        return file_content

def count_words(file_words):
    file_list = file_words.split()
    return len(file_list)

def count_character(book_content):
    char_dict = {}
    
    for text in book_content.split():
        lower_text = text.lower()
        for char in lower_text:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] +=1
                else:
                    char_dict[char] = 1
    return char_dict

def sort_on(char_dict):
    return char_dict["num"]

def print_report(book_path, char_dict, num_word):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_word} words found in the doxument")
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
        print(f"The {character} character was found {value} times")
        
    print("--- End report ---")


if __name__ == "__main__":
    main()
