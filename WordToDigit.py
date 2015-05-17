##Status: solved
##problem: https://www.codeeval.com/open_challenges/104/
##Having a string representation of a set of numbers you need to print this numbers.
##
##solution: created a dictionary to associate the word for a number with the number itself.
##then i just ran the dictionary for every word in the input separated by the ;

digitdictionary = {'zero':str(0), 'one':str(1), 'two':str(2),'three':str(3), 'four':str(4),'five':str(5), 'six':str(6), 'seven':str(7), 'eight':str(8),'nine':str(9)}
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print("".join([digitdictionary[i] for i in test[:-1].split(";")]))
test_cases.close()
