##Status: Solved
##https://www.codeeval.com/open_challenges/112/
##You are given a list of numbers which is supplemented with positions that have to be swapped.
##
##Solution: I split the input into the code and the swapping directions, then i perform the swapping action for each swapping direction(seen in the for i loop
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    message = test.split(":")[0][:-1].split(" ")
    for i in test[:-1].split(":")[1][1:].split(", "):
        j, k = int(i[:i.index("-")]), int(i[i.index("-")+1:])
        message[j],message[k] = message[k],message[j]
    print(" ".join(message))
test_cases.close()
