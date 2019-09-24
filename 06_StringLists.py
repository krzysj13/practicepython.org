'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

'''
print('Program will return that your word is palindrome.')
string = input('Please, type your word: ')
string_reversed = string[::-1]

if string == string_reversed:
  print('Your word is palindrome!')
else:
  print('Your word is not palindrome!')
