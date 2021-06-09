import random

def match_letter(letter_entered, word):
  idx_from_word = []
  for idx, letter in enumerate(word):
    if letter == letter_entered:
      idx_from_word.append(idx)
  
  print("Word: " + word + " - Indices que matchean: " +  str(idx_from_word))
  

def run():
  letter = input("Ingrese una letra: ")

  with open("./data.txt", "r", encoding="utf-8") as f:
    allText = f.read()
    selectedWord = random.choice(allText.split())
    match_letter(letter, selectedWord)


if __name__ == "__main__":
  run()