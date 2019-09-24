'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

name = str(input('Type your name: '))
age = int(input("Type your age: "))
ageDiff = str(100-age)
print(name + ' you will get 100 years in ' + ageDiff + ' years.')
