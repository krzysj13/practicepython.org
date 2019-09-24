''' 
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''

number = int(input('Type your number: '))

for i in range(2, number):
  if number % i == 0:
    print('Number is prime!')
    break
  elif i == number-1:
    print('Number is not prime!')
