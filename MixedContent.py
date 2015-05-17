##status: solved
##Problem: https://www.codeeval.com/open_challenges/115/
##You have a string of words and digits divided by comma. Write a program which separates words with digits. You shouldn't change the order elements.


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    message = [[],[]]
#This for loop will separate numbers and non numbers into the message 2d matrix
    for i in test[:-1].split(","):
        if i.isdigit():
            message[1].append(i)
        else:
            message[0].append(i)
#This will print it as desired w/ | as a divisor only if there are both words and numbers
    if len(message[0])!=0 and len(message[1])!=0:
        print("|".join([",".join(message[0]), ",".join(message[1])]))
    else:
        print("".join([",".join(message[0]), ",".join(message[1])]))
test_cases.close()
