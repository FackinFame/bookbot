from stats import get_num_words
from stats import gets_num_characters
from stats import sort_char_count
import sys
if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = gets_num_characters(text)
    sorted_num_char_dict = sort_char_count(gets_num_characters(text))
    ##sorted_characters = sort_characters(num_characters)
    ##print statements to show the user the results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    ##print(sorted_num_char_dict)
    for key, value in sorted_num_char_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")
                              
def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()
    
