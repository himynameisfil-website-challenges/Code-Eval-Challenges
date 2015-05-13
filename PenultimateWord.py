##status: solved
##problem : https://www.codeeval.com/open_challenges/92/
##Write a program which finds the next-to-last word in a string.
##
##Basically, the print statment splits the string into words and prints the 2nd one(counting from the end)
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print(test.split(" ")[-2])
test_cases.close()
