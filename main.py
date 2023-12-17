def main():
    file_name = "books/frankenstein.txt"
    file_contents = read_file(file_name)
    word_count = len(file_contents.split())
    char_count = count_characters(file_contents.lower())
    print_report(file_name, word_count, char_count)
    
def read_file(file_name):
    with open(file_name) as f:
        return f.read()

def count_characters(file_contents):
    char_count = {}
    for char in file_contents:
        if not char.isalpha():
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_report(file_name, word_count, char_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    sorted_char_count = dict(sorted(char_count.items(), key = lambda item: item[1], reverse = True))
    for char in sorted_char_count:
        print(f"The '{char}' character was found {sorted_char_count[char]} times")
    print("--- End report ---")
    

if __name__ == "__main__":
    main()