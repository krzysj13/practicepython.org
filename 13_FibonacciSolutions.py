'''
  Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''
def generateFibonacci():
    inputNumber = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if inputNumber == 0:
        FibonnaciSequence = []
    elif inputNumber == 1:
        FibonnaciSequence = [1]
    elif inputNumber == 2:
        FibonnaciSequence = [1,1]
    elif inputNumber > 2:
        FibonnaciSequence = [1,1]
        while i < (inputNumber - 1):
            FibonnaciSequence.append(FibonnaciSequence[i] + FibonnaciSequence[i-1])
            i += 1

    return FibonnaciSequence
