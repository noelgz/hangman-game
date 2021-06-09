import random
import os

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

def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def run():
  clear_screen()
  print("¡ Adivina la palabra !")

  selectedWord = random_word()
  underscore = ""
  for i in range(1, len(selectedWord) + 1):
      underscore = underscore + "_ "
  
  print(underscore)
  letter = input("\nIngrese una letra: ")


if __name__ == "__main__":
  run()