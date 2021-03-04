from cocanb_to_english import cocanb_to_english
from english_to_cocanb import english_to_cocanb
from config import view_config, change_config

def cocanb_or_english():
    choose_lang = input("Would you like to translate Cocánb to English, translate English to Cocánb or configure your settings? Press[1/2/3/4]: ")
    if choose_lang == "1":
      cocanb_to_english()
    elif choose_lang == "2":
      english_to_cocanb()
    elif choose_lang == "3":
      
    else:
        print("Please enter a valid input.")
        cocanb_or_english()
    input("Press enter to exit.")

cocanb_or_english()

input("Press enter to exit.")