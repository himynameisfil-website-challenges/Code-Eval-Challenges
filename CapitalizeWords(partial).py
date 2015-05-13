##status: partially
##problem : https://www.codeeval.com/open_challenges/93/
##Write a program which capitalizes the first letter of each word in a sentence
## This will break down the string into each word of the array and capitalize the first letter
#then it will join it all together w/ spaces

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print(" ".join([i.capitalize() for i in test[:-1].split(" ")]))
test_cases.close()
