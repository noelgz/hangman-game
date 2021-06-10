import random
import os
import unicodedata

SELECTED_WORD = ""
COMPLETE_WORD = []

# Get a random word from the .txt file
def random_word():
  with open("./data.txt", "r", encoding="utf-8") as f:
    allText = f.read()
    selectedWord = random.choice(allText.split())

  return selectedWord 

def match_letter(letter_entered):
  global COMPLETE_WORD

  for idx, letter in enumerate(SELECTED_WORD):
    if unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore') == unicodedata.normalize('NFKD', letter_entered).encode('ASCII', 'ignore'):
      COMPLETE_WORD[idx]=letter

  return COMPLETE_WORD

def draw_new_screen():
  global COMPLETE_WORD
  clear_screen()
  print("¡ Adivina la palabra !")

  for letter in COMPLETE_WORD:
    print (letter, end = ' ')

# Clear the terminal screen 
def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

# The main function
def run():
  clear_screen()
  print("¡ Adivina la palabra !")
  global SELECTED_WORD
  global COMPLETE_WORD
  SELECTED_WORD = random_word()

  for i in range(1, len(SELECTED_WORD) + 1):
      COMPLETE_WORD.append("_")
      print (end = '_ ')
  
  while "_" in COMPLETE_WORD:
    letter = input("\n\nIngrese una letra: ")

    wordMatch = match_letter(letter)
    draw_new_screen()
  
  clear_screen()
  print("\n\n¡ GANASTE !")


if __name__ == "__main__":
  run()