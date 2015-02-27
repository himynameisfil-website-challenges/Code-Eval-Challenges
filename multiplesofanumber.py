# Code-Eval-Challenges
challenge problems found on codeeval
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
