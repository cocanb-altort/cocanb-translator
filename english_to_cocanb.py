

def cocanbise(string):
    # split string into words
    initial_list = " ".split(string)

    # count letters of each word
    word_counts = []
    for word in initial_list:
        word_counts.append(len(word))

def english_to_cocanb():
    initial_phrase = input("Please enter your English Phrase: ")
    sentences = ".".split(initial_phrase)
    for sentence in sentences:
        cocanbise(sentence)