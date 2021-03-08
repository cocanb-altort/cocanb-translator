import json

with open("config.json") as config:
  data = json.load(config)

# View the punctuation configuration
def view_config():
  print("Quotation indicator: " + data["quotation_symbol"])
  print("Sentence separator: " + data["sentence_break_symbol"])

# Edit the punctuation con
def change_config(): #TODO: this needs to stay changed after closing
  config_input = input("What would you like to change? [q: quotation indicator, p: sentence separator]")
  if config_input == "q":
    new = input("What would you like to change it to?")
    data["quotation_symbol"] = new
  elif config_input == "p":
    new = input("What would you like to change it to?")
    data["sentence_break_symbol"] = new
  else:
    print("Please enter a valid input.")
    change_config()