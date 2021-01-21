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
        y = ["y","ý","ÿ"]
        h = ["h","ħ"]
        w = ["w","ŵ"]
        c = ["c","č","ç"]
        r = ["r","ř"]
        s = ["s","š"]
        n = ["n","ň"]
        d = ["d","đ"]
        l = ["l","ł"]
        g = ["g","ğ"]
        
        # add more diacritics
        result_without_diacritics = " ".join(result)
        final_result = result_without_diacritics.replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("g", random.choice(g), 1).replace("l", random.choice(l), 1).replace("d", random.choice(d), 1).replace("n", random.choice(n), 1).replace("s", random.choice(s), 1).replace("r", random.choice(r), 1).replace("c", random.choice(c), 1).replace("w", random.choice(w), 1).replace("h", random.choice(h), 1).replace("a", random.choice(a), 1).replace("e", random.choice(e), 1).replace("i", random.choice(i), 1).replace("o", random.choice(o), 1).replace("u", random.choice(u), 1).replace("y", random.choice(y), 1).replace("ae", "æ").replace("oe", "œ")
        print(final_result)
    else:
        print("Please enter a valid input.")
        cocanb_or_english()

cocanb_or_english()

input("Press any key to exit.")
