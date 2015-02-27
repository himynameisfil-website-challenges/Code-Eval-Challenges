# Code-Eval-Challenges
challenge problems found on codeeval
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
