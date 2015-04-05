##Status:Solved
##Problem:https://www.codeeval.com/open_challenges/22/
##The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0, print out the F(n).

#The function will determine the n'th fibonacci number using the golden ratio
import sys
goldratio = (1 + 5**.5)/2
antigoldratio = (1 - 5**.5)/2
def fibonacci(n):
    x = (goldratio**n - antigoldratio**n) / (5**.5)
    return int(x)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    print(fibonacci(int(test)))

test_cases.close()
