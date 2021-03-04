from cocanb_to_english import cocanb_to_english
from english_to_cocanb import english_to_cocanb

def cocanb_or_english():
    choose_lang = input("Would you like to translate Cocánb to English or English to Cocánb? Press[c/e]: ")
    if choose_lang == "c":
        cocanb_to_english()
    elif choose_lang == "e":
        english_to_cocanb()
    else:
        print("Please enter a valid input.")
        cocanb_or_english()
    input("Press enter to exit.")

cocanb_or_english()

input("Press enter to exit.")
