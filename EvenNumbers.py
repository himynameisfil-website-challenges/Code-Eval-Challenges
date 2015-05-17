#status: solved
#problem: https://www.codeeval.com/open_challenges/100/
#Write a program which checks input numbers and determines whether a number is even or not.

#Solution: Even/ odd test is easily done via mod 2 and you can switch even = 0 and odd= 1 to even = 1 and odd = 0 by adding 1 to the number
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  try:
    print((int(test[:-1])+1)%2)
  except:
    break
test_cases.close()
