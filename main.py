#Reads book file and then prints it all to console
import sys
from collections import Counter

def main():
    open_file()
    read_file()

file_name = sys.argv[1]
file_path = f"books/{file_name}"
print(f"----BEGIN BOOK REPORT OF {file_path}-----")

def open_file():
    if len(sys.argv) < 2:
        print("Expected usage: python main.py <filename>")
        return
       

    try:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
        

    except FileNotFoundError:
        print(f"The file {file_name} does not exist in the BOOKS directory.")

def sort_on(dict):
    return dict[1]

def read_file():
    file_contents = open_file()
    contents = file_contents.split()
    counts = len(contents)
    
    print(f"There are {counts} words in this book.")

    char_count = Counter(file_contents.lower())
    
    print("Character Frequency:")

    listed_dict = list(char_count.items())
    listed_dict.sort(reverse=True, key=sort_on)


    for character, count in listed_dict:
        if character.isalpha():
            print(f"The {character} character appeared {count} times.")
        else:
            continue
    print("----END REPORT----")


if __name__ == '__main__':
    main()