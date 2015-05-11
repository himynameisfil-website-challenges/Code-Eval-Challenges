#status: solved
#Problem: https://www.codeeval.com/open_challenges/67/
#You will be given a hexadecimal (base 16) number. Convert it into decimal (base 10).

#this is my dictionary that will associate the number/letter with it's equivalent value base 10
x = {chr(i):(i-87) for i in range(97,97+6)}
x.update({chr(i):(i-48) for i in range(48,48+10)})

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    #This will create a list of the digit and find it's equivalent in base 10
    #E.G. for the number 9f, the f = 15*(16^0) and the 9 = 9*(16^1)
    print(sum([x[test[i]]*(16**(len(test[:-1])-i-1)) for i in range(0,len(test[:-1]))]))

test_cases.close()
