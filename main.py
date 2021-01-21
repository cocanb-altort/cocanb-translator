import unidecode
import numpy

choose_lang = input("Would you like to translate Cocánb to English or English to Cocánb? Press[c/e]")

def cocanb_or_english()
    if choose_lang == c:
        string_with_diacritics = input("Please input your Cocánb phrase: ")
        string = unidecode.unidecode(string_with_diacritics)
        print("This doesn't work yet")
    elif choose_lang == e:
        string = input("Please input your English phrase: ")
        string_list = string.split(" ")
        end_letters = []
        lengths = []
        for i in string_list:
            string_list[i] = string_list[i].split("")
            lengths.append(chr(ord('`')+len(string_list[i])))
            end_letters.append(string_list[i][-1])
    else:
        print("Please enter a valid input.")
        cocanb_or_english()

cocanb_or_english()

input("Press any key to exit.")
