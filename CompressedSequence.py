##status: Solved
##Problem: https://www.codeeval.com/open_challenges/128/
##Assume that someone dictates you a sequence of numbers, and you need to write it down. For brevity, he dictates it as follows: first he dictates the number of consecutive identical numbers, and then - the number itself.


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    test = test[:-1].split(" ")
    start, output = 0, []
#So you need to determine how many times a number repeats and what number is being repeated
#The start variable tracks how many times something repeats by comparing a start point to a point where a number changes ( index of current change - index of last change)
#then it'll add the repitition count and number being repeated to the output array. afterwards, it'll do this for the last set of numbers and print it
    for i in range(1,len(test)):
        if test[i]!=test[i-1]:
            output.extend((str(i -start),test[i-1]))
            start = i
    output.extend((str(len(test)-start),test[len(test)-1]))
    print(" ".join(output))
test_cases.close()
