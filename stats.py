
def get_num_words(text):
    num_words = (text.split())
    return len(num_words)

def gets_num_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_char_count(char_count):
    sorted_num_characters = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    sorted_num_characters_alpha = {}
    for chars in sorted_num_characters:
        if chars.isalpha():
            sorted_num_characters_alpha[chars] = sorted_num_characters[chars]
        else:
            pass
    return sorted_num_characters_alpha
    
def print_sorted_alpha(sorted_num_characters_alpha):
    for char, num in sorted_num_characters_alpha:
        print(f"{char}:  {num}")
    
    

    


