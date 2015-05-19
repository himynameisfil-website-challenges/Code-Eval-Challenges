#status: solved
#problem: https://www.codeeval.com/open_challenges/131/
#You are given a number N and a pattern. The pattern consists of lowercase latin letters and one operation "+" or "-". The challenge is to split the number and evaluate it according to this pattern e.g. 
#1232 ab+cd -> a:1, b:2, c:3, d:2 -> 12+32 -> 44

#Solution: this function will see where the operation is in the second half of the input
#then it will split the first part into two based off of where the operation was
#Then it will add or subtract it according to the operation found
def split(x,y):
    index = [i for i in range(0,len(y)) if y[i]=="+" or y[i]=="-"]
    first,second = int(x[:index[0]]), int(x[index[0]:])
    if "+" in y:
        print(first+second)
    else:
        print(first - second)
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test=="":
        break
    split(test.split(" ")[0],test[:-1].split(" ")[1])
test_cases.close()
