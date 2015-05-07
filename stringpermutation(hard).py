#status: done
#problem:https://www.codeeval.com/open_challenges/14/
#Write a program which prints all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order.

#This program will first create an array with each letter/number as its own element.
#the loop will replace the array with each permutation with an additional letter(that hasn't been used before)
#the  loop will continue till the length of the permutation matches the length of the test case
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    arr = [i for i in test[:-1]]
    while len(arr[0])!=len(test[:-1]):
        arr = [i+j for i in arr for j in test[:-1] if not j in i]
    arr.sort()
    print(",".join(arr))
test_cases.close()
