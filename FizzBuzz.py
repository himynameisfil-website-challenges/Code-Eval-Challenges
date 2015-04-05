##Status:Solved
##Problem:https://www.codeeval.com/open_challenges/1/
##Players generally sit in a circle. The first player says the number “1”, and each player says next number in turn. However, any number divisible by X (for example, three) is replaced by the word fizz, and any divisible by Y (for example, five) by the word buzz. Numbers divisible by both become fizz buzz. A player who hesitates, or makes a mistake is eliminated from the game.
##Write a program that prints out the final series of numbers where those divisible by X, Y and both are replaced by “F” for fizz, “B” for buzz and “FB” for fizz buzz.

#This will take the file input and take the three numbers in a line and assign
#the first number to fizz, second to buzz, and the 3rd to the range
#Then the program will see if a number is dvisiabble by both fizz/buzz, fizz, or buzz and output a number/letter according to the directions of the problem
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    x=test.split(" ")
    fizz = int(x[0])
    buzz = int(x[1])
    n = (x[2])
    for i in range(1,n+1):
        if i % fizz ==0 and i % buzz == 0:
            print("FB", end = " ")
        elif i % fizz == 0:
            print("F", end = " ")
        elif i % buzz == 0:
            print("B", end = " ")
        else:
            print(i, end = " ")
    print("\n")

test_cases.close()
