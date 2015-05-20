##status: partially solved
##https://www.codeeval.com/open_challenge_scores/?pkbid=196
##Write a program that, given a sentence where each word has a single digit positive integer as a prefix and suffix, swaps the numbers while retaining the word in between. Words in the sentence are delimited from each other by a space.
##
##Considering it's effectively a 1 liner, idk how i can make this more efficient
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print(" ".join([i[-1]+i[1:-1] +i[0] for i in test[:-1].split(" ")]))
test_cases.close()
