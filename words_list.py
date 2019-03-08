# words_list.py
# ---------------------------
# From a text file, creat list of passwords/word/phrases/numbers want to encrypt

import random

# Returns a list of 'words'
def words_list_fn():
    # Give File with the words want to encrypt
    #   Given either passwords.txt or top-1000000-passwords.txt
    f = "top-1000000-passwords.txt"
    # f = "passwords.txt"
    file = open(f, "r", encoding='utf-8-sig')
    words = []

    # Add each 'word' to list
    for line in file:
        word = line.split('\n')[0]
        if len(word) <= 16: words += [word]
    return  words

# Returns a random 'word' from word list
def randompass(words):
    randy = random.randint(0,len(words)-1)
    return words[randy]