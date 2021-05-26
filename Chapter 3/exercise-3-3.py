# Write a function that draws a grid like the following:
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence of values:

def topAndBottomGrid():
    print('+', '- '* 5, '+', '- '* 5, '+')

def leftAndRightGrid():
    for i in range(4):
        print('|',' '* 10, '|',' '* 10, '|',' '* 10)

def twoByTwoGrid():
    for i in range(2):
        topAndBottomGrid()
        leftAndRightGrid()
    topAndBottomGrid()

twoByTwoGrid()
