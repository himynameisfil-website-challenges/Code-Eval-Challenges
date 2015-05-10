#Status:
#You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.
#https://www.codeeval.com/open_challenges/29/


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if test =="":
    break
  lst = []
  for i in test[:-1].split(","):
    if not i in lst:
      lst.append(i)
  print(",".join(lst))
test_cases.close()
