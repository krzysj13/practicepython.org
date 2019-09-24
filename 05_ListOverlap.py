'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''
import random

#lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
emptyList1 = []
emptyList2 = []
emptyList3 = []
emptyList4 = []

#check that element from list a is in list b
for item in a:
  if item in b:
    emptyList1.append(item)

print('Elements from list a which contains in list b')
print(emptyList1)
print('')

#check that element from list b is in list a
for item in b:
  if item in a:
      emptyList2.append(item)

print('Elements from list b which contains in list a')
print(emptyList2)
print('')

# 2 random list
a_rand = [random.randint(0,10) for i in range(5)]
b_rand = [random.randint(0,20) for i in range(10)]

print(a_rand)
print(b_rand)

for item in a_rand:
  if item in b_rand:
    emptyList3.append(item)

for item in b_rand:
  if item in a_rand:
    emptyList4.append(item)

print('Elements from list a generated randomly which contains in list b generated randomly.')
print(emptyList3)
print('')

print('Elements from list b generated randomly which contains in list b generated randomly.')
print(emptyList4)
print('')




