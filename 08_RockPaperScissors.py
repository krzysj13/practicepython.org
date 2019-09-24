''' 
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
  Rock beats scissors
  Scissors beats paper
  Paper beats rock
'''

import random

#scores
player1 = 0
player2 = 0


def getInput():
  global player
  player = int(input('Type your number: '))
  if not (player == 1 or player == 2 or player == 3):
        print('Typed number is not 1 or 2 or 3.')
        getInput()


def compare(p1, p2):
  global player1
  global player2

  if (p1 == 1 and p2 == 1) or (p1 == 2 and p2 == 2) or (p1 == 3 and p2 == 3):
    print('tie')
  elif (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 ==3 and p2 == 2):
    print('Player win!')
    player1 = player1 + 1
  else:
    print('CPU win!')
    player2 = player2 + 1
  
  return player1, player2


def game():
  while(not(player1==3 or player2 == 3)):
    getInput()
    cpu_player = random.randint(1,3)
    compare(player, cpu_player)
    
    #print score
    print('\nScore: Player: ' + str(player1) + '\nCPU:' + str(player2))

  if player1 == 3:
    print('Player win a game!')
  else:
    print('CPU win, lets try again.')

print('We are playing to 3 wins! \nChoose paper (1) / scisors (2) / rock (3)\nRemember the rules:\nRock beats scissors\nScissor beats paper\nPaper beats rock.')

game()
#play again
print('One more time?')
oneMoreTime = input('Please type "y" if you want player again, oraz press CTRL+C to exit. ' )

if oneMoreTime == 'y':
  game()
else:
  print('Something wrong!')
  


