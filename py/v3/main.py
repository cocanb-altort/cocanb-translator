#from cocanb_to_english import cocanb_to_english
#from english_to_cocanb import english_to_cocanb
#from config import view_config, change_config

import tkinter as tk

window = tk.Tk()

text = tk.Label(text="Welcome to the Cocánb Translator.\nWélćomt thCocántra ňslâtono negôbec bfřj.")

ec_button = tk.Button(text="Translate English to Cocánb")

ce_button = tk.Button(text="Translate Cocánb to English")

config_button = tk.Button(text="Settings")

text.pack()

ec_button.pack()

ce_button.pack()

config_button.pack()

window.mainloop()