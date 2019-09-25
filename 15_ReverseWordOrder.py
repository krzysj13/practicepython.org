'''
  Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
  Then I would see the string:
  Michele is name My
  shown back to me.
'''
inputString1 = 'My name is Michele.'
inputString2 = 'Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.'
inputString3 = 'Ala ma kota kota ma Ale'




def reverseString(inputString):
  if inputString[-1] == '.':
    inputStringWithoutDot = inputString.replace('.', '')
    inputStringSplitted = inputStringWithoutDot.split(' ')
    inputStringToList = inputStringSplitted[::-1]
    inputStringReversed = ' '.join(inputStringToList) + '.'
    print(inputStringReversed)
  else:
    inputStringWithoutDot = inputString
    inputStringSplitted = inputStringWithoutDot.split(' ')
    inputStringToList = inputStringSplitted[::-1]
    inputStringReversed = ' '.join(inputStringToList) + '.'
    print(inputStringReversed)

reverseString(inputString1)
reverseString(inputString2)
reverseString(inputString3)


