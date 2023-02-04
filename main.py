#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo 
import random as rnd 
from replit import clear

USER_LIVES = 0
HARD_MODE = 5
EASY_MODE = 10

NUMBER_TO_GUESS = 0

# if GAME = True - play on, False - play off 
GAME_STATUS = True

def randNumberToGuess():
  global NUMBER_TO_GUESS
  NUMBER_TO_GUESS = rnd.randint(1, 100)


def choseGameLevel(level):
  global USER_LIVES
  USER_LIVES = 0
  
  if level == 'easy':
    USER_LIVES = EASY_MODE
  elif level == 'hard':
    USER_LIVES = HARD_MODE
  else:
    print("Wrong level chose!")
    return False

  return True


def userNumberLowHigh(number):
  if number > NUMBER_TO_GUESS:
    print("Too high.")
  else:
    print("Too low.")

  userLivesMinus()


def userNumberEqual(number):
  if number == NUMBER_TO_GUESS:
    global GAME_STATUS
    GAME_STATUS = False
    
    print("You win!")
    return True
  else:
    userNumberLowHigh(number)

  return False


def userLivesMinus():
  global USER_LIVES
  USER_LIVES -= 1
  print(f"You have {USER_LIVES} attempts remaining to guess the number.")
  checkUserLives()


def checkUserLives():
  global USER_LIVES

  if USER_LIVES == 0:
    global GAME_STATUS
    GAME_STATUS = False
    print("You lose!")

def game():
  # clear scr 
  clear()

  # print logo
  print(logo)

  # get number to guess 
  randNumberToGuess()

  # print welcome msg 
  print("""Welcome to the Guessing Game!
  I'm thinking of a number between 1 and 100.""")

  # chose game level
  flag_rigth_dif_level = False
  
  while flag_rigth_dif_level == False:
    flag_rigth_dif_level = choseGameLevel(input("Choose a difficulity. Type 'easy' or 'hard': "))

  # loop to guess
  while GAME_STATUS == True:
    while True:
      try:
        user_number = int(input("Make a guess: "))
        break
      except ValueError:
        print("You need type a number!")      
  
    userNumberEqual(user_number)

# start game and new game at the end 
while GAME_STATUS == True:
  game()
  
  print("")
  if input("Play one more time? Typy 'y' to yes, 'n' to no: ") == 'y':
    GAME_STATUS = True
  else: 
    GAME_STATUS = False
  
