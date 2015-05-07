##Status:solved
##Problem:https://www.codeeval.com/open_challenges/30/
##Print the intersection of two sets of numbers.
#line 10 is effectively (I'll take a look at the first half of the numbers, see if it's in the second half, if it is. it's a part of this list
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
      break
    lst = [i for i in test.split(";")[0].split(",") if i in test.split(";")[1][:-1].split(",")]
    print(",".join(lst))

test_cases.close()
