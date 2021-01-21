import unidecode

choose_lang = input("Would you like to translate Cocánb to English or English to Cocánb? Press[c/e]")

def cocanb_or_english()
    if choose_lang == c:
        string_with_diacritics = input("Please input your Cocánb phrase: ")
        string = unidecode.unidecode(string_with_diacritics)
        # do this
    elif choose_lang == e:
        string = input("Please input your English phrase: ")
        # and this
    else:
        print("Please enter a valid input.")
        cocanb_or_english()

cocanb_or_english()

input("Press any key to exit.")
