##Status:Solved
##Problem:https://www.codeeval.com/open_challenges/20/
##Given a string write a program to convert it into lowercase.


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    x = test.lower()
    print(x)

test_cases.close()
