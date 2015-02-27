# Code-Eval-Challenges
challenge problems found on codeeval
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    x = test.split()
    x.reverse()
    for i in range(len(x)):
        print(x[i], end = " ")
    print( "\n")
test_cases.close
