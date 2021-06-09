import random

def random_word():
  with open("./data.txt", "r", encoding="utf-8") as f:
    allText = f.read()
    selectedWord = random.choice(allText.split())

  return selectedWord 

def match_letter(letter_entered, word):
  idx_from_word = []
  for idx, letter in enumerate(word):
    if letter == letter_entered:
      idx_from_word.append(idx)

  return idx_from_word

def draw_underscore_of_word(word):
  lengthWord = len(word)
  undescoreWord = []
  for i in range(1,lengthWord):
    undescoreWord.append("_")

  return undescoreWord


def run():
  selectedWord = random_word()
  underscore = ""
  for i in range(1, len(selectedWord) + 1):
      underscore = underscore + "_ "
    
  print(selectedWord)
  print(underscore)

  #letter = input("Ingrese una letra: ")


if __name__ == "__main__":
  run()