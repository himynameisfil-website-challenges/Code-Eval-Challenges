##status: Solved
##Problem: https://www.codeeval.com/open_challenges/122/
##In this challenge you're given a random string containing hidden and visible digits. The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9 is behind 'j'. Any other symbol in the string means nothing and has to be ignored. So the challenge is to find all visible and hidden digits in the string and print them out in order of their appearance.

#These lines create a dictionary that associates the letters with digits and digits with themselves
alphabet,numbers = "abcdefghij", "0123456789"
HiddenDict = dict([[alphabet[i],numbers[i]] for i in range(len(numbers))])
HiddenDict.update(dict([[numbers[i],numbers[i]] for i in range(len(numbers))]))


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
#This will use the dictionary to get our hidden digits and print it as long as there was a hidden digit( prints NONE if there were none)
    test="".join([HiddenDict[i] for i in test[:-1] if i in alphabet or  i in numbers])
    if test =="":
        print("NONE")
    else:
        print(test)
test_cases.close()
