'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

print('Hi, program will check that your number is odd or even, and also check divides evenyl into number.')
num = int(input('Please type your number: '))
div = int(input('Please type your divides number: '))

if num % 2 == 0:
  if num % 4 != 0:
    print('Your number is even.')
  else:
    print('Your number is even and multiple of 4.')
elif num % 2 != 0:
  print('Your number is odd.')

if num % div == 0:
  print('Your numbers divides evenly.')
else:
  print('Your numbers doesnt divides evenly.')
