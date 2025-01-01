def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    x = file_contents.split()
    b = len(x)
    print(b)

def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lowered_string = file_contents.lower()

    char_counts = {}
    for char in lowered_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts  # Only return the result, don't print here

# Call main to count words
main()

# Call count_characters and print the result outside the function
char_counts = count_characters()
print(char_counts)

def print_report():
    word_count = main()
    char_counts = count_characters()
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char, count in sorted_char_counts:
        if char.isalpha():  # Only include alphabetic characters
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":
    print_report()