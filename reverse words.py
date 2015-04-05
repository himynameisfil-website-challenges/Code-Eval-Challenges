##Status:Solved
##Problem:https://www.codeeval.com/open_challenges/8/
##Reversing an input sequence of words.

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
