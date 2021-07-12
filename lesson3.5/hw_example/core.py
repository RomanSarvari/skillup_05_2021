import string

letters_to_find = 'aeiouy'

file_1 = "./1.txt"
file_2 = "./2.txt"

def get_file_lines(filename: str) -> list:
    with open(filename) as f:
        return f.readlines()

def get_stats(text: str) -> dict:
    stats = {"vowels": 0, "no_vowels": 0}

    for i in text:
        if i in letters_to_find:
            stats["vowels"] += 1
        else:
            if not i.isdigit() and i not in string.punctuation:
                stats["no_vowels"] += 1
    return stats

file1_lines = get_file_lines(file_1)
file2_lines = get_file_lines(file_2)

file1_chars = "".join(file1_lines)
file2_chars = "".join(file2_lines)

file1_stat = get_stats(file1_chars)
file2_stat = get_stats(file2_chars)

