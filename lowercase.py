# Code-Eval-Challenges
challenge problems found on codeeval
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    x = test.lower()
    print(x)

test_cases.close()
