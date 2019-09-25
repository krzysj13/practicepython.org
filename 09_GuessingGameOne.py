'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:
  1.Keep the game going until the user types “exit”
  2.Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

score = 0

def getInput():
  global player_number
  player_number = int(input('type your number: '))
  return player_number

def randomNumber():
  global random_number
  random_number = random.randint(1,9)
  return random_number

def getScore():
  global score
  score = score + 1
  print('Your score is ' + str(score) + ' points!\n')
  return score

def compareVariables():
  if player_number == random_number:
    print('You win!')
    getScore()
    Game()
  elif player_number > random_number and player_number <=1 and player_number >= 9:
    print('Too high!')
    getInput()
    compareVariables()
  elif player_number < random_number and player_number <=1 and player_number >= 9:
    print('Too low!')
    getInput()
    compareVariables()
  else:
    print('Type number between 1 and 9')
    getInput()
    compareVariables()

def Game():
  randomNumber()
  print(random_number)
  getInput()
  compareVariables()

print('Gues number between 1 and 9 included.\nGame will say that your number is too low or too high or exactly right.')  
Game()
