 def modify(word: list):
  to_remove = []

  for i in range(len(word)):
    if not word[i].isalnum() and word[i] != '"':
      to_remove.append(word[i])

  word = "".join(word)

  for char in to_remove:
    word = word.replace(char, '')

  return word
