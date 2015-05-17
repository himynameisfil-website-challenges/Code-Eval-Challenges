##Status: solved
##problem: https://www.codeeval.com/open_challenges/111/
##In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one
##
##solution: This will go through each word and if the word in question is larger than anything before it, it will become the current largest word
##after it goes through all words, it just prints the largest word
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    longest, message = 0, ""
    for i in test[:-1].split(" "):
        if len(i)>longest:
            longest, message = len(i),i
    print(message)
test_cases.close()
