##Status: solved
##problem:https://www.codeeval.com/open_challenges/132/
##The major element in a sequence with the length of L is the element which appears in a sequence more than L/2 times. The challenge is to find that element in a sequence.
##
##solution: so i put each number into an array, then looked at the first half +1 and counted how many times it shows up on the list
##if it shows up more than half the time, it's the major element
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test=="":
        break
    test = test[:-1].split(",")
    for i in test[:len(test)//2+1]:
        if test.count(i)>len(test)/2:
            print(i)
            break
    else:
        print("None")
test_cases.close()
