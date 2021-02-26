#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = ""

import random
random_num = random.randint(1, 100)
if (random_num < 33):
  chosen_word = word_list[0]
elif (random_num < 66):
  chosen_word = word_list[1]
else:
  chosen_word = word_list[2]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

def check_guess() :
  for letter in chosen_word:
    if (guess == letter):
      return True
  return False
