##Status:Partially completed
##Problem:https://www.codeeval.com/open_challenges/24/
##Print the sum of integers read from a file.

import sys
lst = []
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    lst.append(int(test))
print(sum(lst))

test_cases.close()
