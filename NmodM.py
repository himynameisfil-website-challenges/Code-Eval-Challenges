#Status: solved
#Problem: https://www.codeeval.com/open_challenges/62/
#Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

#Solution: I define both numbers into N and M. I find the remainder by flooring N/M, multiplying it by M, and finding the difference between that and N
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    N = int(test[:-1].split(",")[0])
    M = int(test[:-1].split(",")[1])
    print(N-M*(N//M))

test_cases.close()
