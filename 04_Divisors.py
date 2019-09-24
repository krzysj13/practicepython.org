'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

# empty list
list = []

print('Hi, program will return all divisors of your number.')
number = int(input('Please type your number: '))

for item in range(1, number):
  if number % item == 0:
    list.append(item)

print('List of divisors of your number.')
print(list)
