import os
import random
import unicodedata

def clear_screen(self):
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

class HangmanGame:
  """ It contains all the logic of the game """

  def __init__(self):
    self.selected_word = ""
    self.complete_word = []

    self._load_word()

  def _load_word(self):
    """ Select a word from the .txt file to play """

    with open ("./data.txt", "r", encoding="utf-8") as f:
      allText = f.read()
      self.selectedWord = random.choice(allText.split())
  
  def draw_scenes(self):
    """ Draw and refresh scenes of the game """
    pass



if __name__ == "__main__":
  game = HangmanGame()

