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


    def cocanbise(string):
        res = []

        # split string into words
        initial_list = " ".split(string)

        # Iterating through every letter of the list
        for w in initial_list:
            res.append(modify(list(w)))

        # count letters of each word
        word_counts = []
        for word in res:
            word_counts.append(len(word))


    def english_to_cocanb():
        initial_phrase = input("Please enter your English Phrase: ")
        sentences = ".".split(initial_phrase)
        for sentence in sentences:
            cocanbise(sentence)
