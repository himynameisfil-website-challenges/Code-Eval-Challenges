##Status:Solved
##Problem:https://www.codeeval.com/open_challenges/18/
##Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    x = test.split(",")
    i=1
    while int(x[0]) > i * int(x[1]):
        i+=1
    print(i * int(x[1]))
test_cases.close()
