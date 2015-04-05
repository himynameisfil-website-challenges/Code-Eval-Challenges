##Status:Partially completed
##Problem:https://www.codeeval.com/open_challenges/30/
##Print the intersection of two sets of numbers.

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    x = test.split(";")
    y = set(x[0].split(","))
    z = set(x[1].split(","))
    a = list((y).intersection(z))
    a.sort()
    for i in a:
        print(i, end = "")
        if i != a[len(a)-1]:
            print(end = ",")
    print()

test_cases.close()
