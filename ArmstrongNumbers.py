#status:solved
#problem:https://www.codeeval.com/open_challenges/82/
#An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input numbers are Armstrong numbers.

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    #int(test[:-1]) is the number the test input gave
    #sum([int(i)**len(test[:-1]) for i in test[:-1] is the sum of a list.
    #The list is composed of digit^(number of digits) for all digits
    print(int(test[:-1])==sum([int(i)**len(test[:-1]) for i in test[:-1]]))
test_cases.close()
