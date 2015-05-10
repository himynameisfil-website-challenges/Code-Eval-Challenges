#status: SOlved
#Problem: You are given a string 'S' and a character 't'. Print out the position of the rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none. The position to be printed out is zero based.
#https://www.codeeval.com/open_challenges/31/
#Solution: since .index() finds the left most character, I just reversed the order of the string, indexed it, and worked from there

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if test =="":
    break
  sequence = test.split(",")[0][::-1]
  character = test.split(",")[1][0]
  if sequence.count(character)==0:
    print(-1)
  else:
    x = sequence.index(character)
    print(len(sequence)-x-1)

test_cases.close()
