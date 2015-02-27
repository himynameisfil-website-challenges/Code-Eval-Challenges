# Code-Eval-Challenges
challenge problems found on codeeval
import sys
lst = []
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    lst.append(int(test))
print(sum(lst))

test_cases.close()
