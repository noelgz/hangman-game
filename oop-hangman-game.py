import os
import random
import unicodedata

def clear_screen():
  """ Clear the terminal screen """
  
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

class HangmanGame:
  """ It contains all the logic of the game """

  def __init__(self):
    self.selectedWord = ""
    self.complete_word = []

    self._load_word()
    self._draw_scenes()


  def _load_word(self):
    """ Select a word from the .txt file to play """

    with open ("./data.txt", "r", encoding="utf-8") as f:
      allText = f.read()
      self.selectedWord = random.choice(allText.split())


  def _draw_scenes(self):
    """ Draw and refresh scenes of the game """

    for i in range(1, len(self.selectedWord) + 1):
      self.complete_word.append("_")
    
    while "_" in self.complete_word:
      clear_screen()
      print("¡ Adivina la palabra !")
      
      for underscore in self.complete_word:
        print(end= underscore+" ")
    
      match = self._match_letter()

    clear_screen()
    print("La palabra era " + self.selectedWord)
    print("\n¡ GANASTE COÑO, ERES UN CRACK AMIOO !")
  

  def _match_letter(self):
    """ Finds if the letter is within the selected word """

    input_letter = self._input_letter()
    for idx,letter in enumerate(self.selectedWord):
      if unicodedata.normalize('NFKD', letter.upper()).encode('ASCII', 'ignore') == unicodedata.normalize('NFKD', input_letter).encode('ASCII', 'ignore'):
        self.complete_word[idx] = letter
    
    return self.complete_word


  def _input_letter(self):
    """ User input data """

    inputLetter = input("\n\nIngrese una letra: ")

    return inputLetter.upper()


if __name__ == "__main__":
  game = HangmanGame()


