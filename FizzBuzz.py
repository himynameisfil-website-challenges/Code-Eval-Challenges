# Code-Eval-Challenges
challenge problems found on codeeval
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    x=test.split(" ")
    fizz = int(x[0])
    buzz = int(x[1])
    n = (x[2])
    for i in range(1,n+1):
        if i % fizz ==0 and i % buzz == 0:
            print("FB", end = " ")
        elif i % fizz == 0:
            print("F", end = " ")
        elif i % buzz == 0:
            print("B", end = " ")
        else:
            print(i, end = " ")
    print("\n")

test_cases.close()
