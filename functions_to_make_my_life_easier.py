import random
import unidecode

def add_diacritics():
    a = ["a", "à", "á", "â", "ä"]
    e = ["e", "è", "é", "ê"]
    i = ["i", "ì", "í", "î"]
    o = ["o", "ò", "ó", "ô", "ö"]
    u = ["u", "ù", "ú", "û", "ü"]
    y = ["y", "ý"]
    g = ["g", "ğ"]
    c = ["c", "č", "ć"]
    s = ["s", "š", "ś"]
    z = ["z", "ž", "ź"]
    n = ["n", "ň"]
    r = ["r", "ř"]
    l = ["l", "ł"]
    d = ["d", "đ"]

def cocanb_to_english():
    print("This does not work yet")

def english_to_cocanb():
    print("This does not work yet")

def cocanb_or_english():
    choose_lang = input("Would you like to translate Cocánb to English or English to Cocánb? Press[c/e]")
    if choose_lang =="c":
        cocanb_to_english()
    elif choose_lang == "e":
        english_to_cocanb()
    else:
        print("Please enter a valid input.")
        cocanb_or_english()
