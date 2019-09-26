'''
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
'''

import random
a = 1
b = 100
playerNumber = 10
score = 0

def getRandom():
  global randNum
  randNum = random.randint(a,b)
  print('is it ' + str(randNum) + '?')
  return randNum

def getInput():
  global playerInput
  playerInput = int(input('Type: '))
  return playerInput

def Game():
  global a
  global b
  global score
  global playerNumber
  
  getRandom()

  if playerNumber == randNum:
    print('WIN!')
    return False

  getInput()
  
  if playerInput == 1:
    b = randNum 
    print('a = ' + str(a) + '  b = ' + str(b) + '\n')
    score += 1
    print('Attempts: ' + str(score))
    Game() 

  if playerInput == 2:
    a = randNum
    print('a = ' + str(a) + '  b = ' + str(b))
    score += 1
    print('Attempts: ' + str(score) + '\n')
    Game()

  return a
  return b
  return score
  return playerNumber


print('If your number is lower type "1", if your number is higher type "2".')
Game()
