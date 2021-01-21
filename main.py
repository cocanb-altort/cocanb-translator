import random

choose_lang = input("Would you like to translate Cocánb to English or English to Cocánb? Press[c/e]")

spaces = ["", "", "", "", r"'", " "]

def cocanb_or_english():
    if choose_lang =="c":
        print("This doesn't work yet")
    elif choose_lang == "e":
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
        a = ["a","ā","ă","ą","ä","à","á","â","ã"]
        e = ["e","ė","ę","ě","ĕ","è","é","ê","ë","ē"]
        i = ["i","ı","į","ī","ï","î","í","ì"]
        o = ["o","ø","õ","ô","ó","ò","ö"]
        u = ["u","ū","ů","ų","ü","ù","ú","û"]
        y = ["y","ý"]
        # add more diacritics
        result_without_diacritics = " ".join(result)
        final_result = result_without_diacritics.replace("a", random.choice(a)).replace("e", random.choice(e)).replace("i", random.choice(i)).replace("o", random.choice(o)).replace("u", random.choice(u)).replace("y", random.choice(y)).replace("ae", "æ").replace("oe", "œ")
        print(final_result)
    else:
        print("Please enter a valid input.")
        cocanb_or_english()

cocanb_or_english()

input("Press any key to exit.")
