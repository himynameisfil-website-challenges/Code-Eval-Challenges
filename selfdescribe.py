#Status: solved
#Problem: https://www.codeeval.com/open_challenges/40/
#A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.

#this function will take the number, and see if a particular digit's position matches with the amount of times it appears in the string
#if at any point it doesn't, it'll return 0. if all check out, it'll return 1
#Then we just have the program call the program for all the test numbers
def selfdescribe(number):
    for i in range(0,len(number)):
        if int(test[i])!= test.count(str(i)):
            return 0
    else:
        return 1
    
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print(selfdescribe(test[:-1]))

test_cases.close()
