#status:solved
#Problem:https://www.codeeval.com/open_challenges/39/
#A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.


#This function will create a list of numbers you get when you sum the squares of the digits
#if a sum of squares is already on the list, the program return 0. if the sum of squares = 1, it'll return 1
#or else it'll update the list and repeat the function
def happyno(lstofsequence,currenttest):
  x = str(currenttest)
  sumsquare = sum([int(i)**2 for i in x])
  if sumsquare ==1:
    return 1
  elif sumsquare in lstofsequence:
    return 0
  else:
    lstofsequence.append(sumsquare)
    return happyno(lstofsequence,sumsquare)

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    lst = []
    print(happyno(lst,int(test[:-1])))
test_cases.close()


