##status: solved
##Problem: https://www.codeeval.com/open_challenges/113/
##You have 2 lists of positive integers. Write a program which multiplies corresponding elements in these lists.

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
#the lines below will turn an input of "9 0 6 | 15 14 9\n"
# into the array                    [[9, 0, 6], [15, 14, 9]]
#Then it will multiply out corresponding numbers and print it in the way the program wants
    test = [[int(i) for i in test.split("|")[0].split(" ") if i.isdigit()] , [int(i) for i in test[:-1].split("|")[1].split(" ") if i.isdigit()]]
    print(" ".join([str(test[0][i]*test[1][i]) for i in range(0,len(test[0]))]))
test_cases.close()
