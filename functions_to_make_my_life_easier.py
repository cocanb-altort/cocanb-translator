import random
import unidecode

def add_diacritics(result):
    a = ["a","a","a","a","a","ā","ă","ą","ä","à","á","â","ã"]
    e = ["e","e","e","e","e","ė","ę","ě","ĕ","è","é","ê","ë","ē"]
    i = ["i","i","i","i","i","ı","į","ī","ï","î","í","ì"]
    o = ["o","o","o","o","o","ø","õ","ô","ó","ò","ö"]
    u = ["u","u","u","u","u","ū","ů","ų","ü","ù","ú","û"]
    y = ["y","y","y","y","y","ý","ÿ"]
    h = ["h","h","h","h","h","ħ"]
    w = ["w","w","w","w","w","ŵ"]
    c = ["c","c","c","c","c","č","ç"]
    r = ["r","r","r","r","r","ř"]
    s = ["s","s","s","s","s","š"]
    n = ["n","n","n","n","n","ň"]
    d = ["d","d","d","d","d","đ"]
    l = ["l","l","l","l","l","ł"]
    g = ["g","g","g","g","g","ğ"]
    result_without_diacritics = " ".join(result)
    result_without_diacritics = result_without_diacritics.replace("oe", "œ").replace("ae", "æ")
    final_result = result_without_diacritics.replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1)
    for index in range(len(result)):
        final_result = final_result.replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1)
    return final_result

def cocanb_to_english():
    string = input("Please input your Cocánb phrase: ")
    new_string = unidecode.unidecode(string).replace(" ", "")
    position_of_separator = new_string.find("non")
    string_list = list(new_string)
    i = len(string_list)
    while i >= position_of_separator + 2:
        # do this

def english_to_cocanb():
    string = input("Please input your English phrase: ")
    string_list = string.split(" ")
    end_letters = []
    lengths = []
    i = 0
    new_string_list = []
    while i <= len(string_list) - 1:
        string_list[i] = list(string_list[i])
        lengths.append(chr(ord('`')+len(string_list[i])))
        end_letters.append(string_list[i][-1])
        del string_list[i][-1]
        new_string_list.append("".join(string_list[i]))
        i = i + 1
    suffix = [None]*(len(end_letters)+len(lengths))
    suffix[::2] = end_letters
    suffix[1::2] = lengths
    output_list = new_string_list + ["non"] + suffix
    output = "".join(output_list)
    insert_points = range (1, len(output))
    selected = random.sample(insert_points, round(len(insert_points) / 4))
    selected.sort()
    selected.append(len(output))
    temp = 0
    result = []
    for i in selected:
        result.append(output[temp:i])
        temp = i
    print(add_diacritics(result))

def cocanb_or_english():
    choose_lang = input("Would you like to translate Cocánb to English or English to Cocánb? Press[c/e]")
    if choose_lang =="c":
        cocanb_to_english()
    elif choose_lang == "e":
        english_to_cocanb()
    else:
        print("Please enter a valid input.")
        cocanb_or_english()
