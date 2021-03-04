import json

# Removes the charachter if it's not letter or num or quotation mark
def modify(word: list):
    to_remove = []

    for i in range(len(word)):
        if not word[i].isalnum() and word[i] != '"':
            to_remove.append(word[i])

    word = "".join(word)

    for char in to_remove:
        word = word.replace(char, '')

    return word


def cocanbise(string: str):
    res = []

    # Splits string into words
    initial_list = " ".split(string)

    # Iterating through every letter of the list
    for w in initial_list:
        res.append(modify(list(w)))

    # Counts letters of each word
    word_counts = []
    for word in res:
        word_counts.append(len(word))

    # Removes last letter of each word and appends to another list

    # Makes suffix list

    # Finds special substrings ("non", "Cocán")

    # Removes capitalisation except first letter of the sentence (and "Cocán")

    # Adds diacritics

    # Joins root + separator + suffix

    # Adds spacing and punctuation

def english_to_cocanb():
    initial_phrase = input("Please enter your English Phrase: ")

    # Separates sentences
    sentences = ".".split(initial_phrase)

    # Counts parity of the quote symbol in each sentence and join two adjacent sentences if both are odd

    # Separates quotes to deal with them separately

    # Magic
    for sentence in sentences:
        cocanbise(sentence)
    
    # Joins the sentences
    output = ". ".join(sentences)

    return output