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
            new_string_list.append("".join(string_list[i])) # this no work
            i = i + 1
        suffix = [None]*(len(end_letters)+len(lengths))
        suffix[::2] = end_letters
        suffix[1::2] = lengths
        output_list = new_string_list + ["non"] + suffix
        output = "".join(output_list)
        insert_points = range (1, len(output))
        selected = random.sample(insert_points, round(len(insert_points) / 4))
        selected.sort()
        selected.append(len(output))  #  include the last slice
        temp = 0  #  start with first slice
        result = []
        for i in selected:
            result.append(output[temp:i])
            temp = i
        print(" ".join(result))
    else:
        print("Please enter a valid input.")
        cocanb_or_english()

cocanb_or_english()

input("Press any key to exit.")
