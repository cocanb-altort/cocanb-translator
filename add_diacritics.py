import random

a_diacritics = ["a", "à", "á", "â", "ä"]
e_diacritics = ["e", "è", "é", "ê"]
i_diacritics = ["i", "ì", "í", "î"]
o_diacritics = ["o", "ò", "ó", "ô", "ö"]
u_diacritics = ["u", "ù", "ú", "û", "ü"]
y_diacritics = ["y", "ý"]
g_diacritics = ["g", "ğ"]
c_diacritics = ["c", "č", "ć"]
s_diacritics = ["s", "š", "ś"]
z_diacritics = ["z", "ž", "ź"]
n_diacritics = ["n", "ň"]
r_diacritics = ["r", "ř"]
l_diacritics = ["l", "ł"]
d_diacritics = ["d", "đ"]

diacritics_dict = {
  "a": a_diacritics,
  "e": e_diacritics,
  "i": i_diacritics,
  "o": o_diacritics,
  "u": u_diacritics,
  "y": y_diacritics,
  "g": g_diacritics,
  "c": c_diacritics,
  "s": s_diacritics,
  "z": z_diacritics,
  "n": n_diacritics,
  "r": r_diacritics,
  "l": l_diacritics,
  "d": d_diacritics
}

def add_diacritics(string: str): #this no work :(
    listed_string = list(string)
    for letter in listed_string:
      for key in diacritics_dict:
        if key == letter:
          letter = random.choice(diacritics_dict[key])
    output_string = "".join(listed_string)
    return output_string