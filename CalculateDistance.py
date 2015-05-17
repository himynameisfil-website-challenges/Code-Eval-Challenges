#status: solved
#Problem: https://www.codeeval.com/open_challenges/99/
#You have coordinates of 2 points and need to find the distance between them.

#line 14 only keeps the numbers, negative signs and spaces, then creates a list of numbers using the space as the split sign. then it calls the distance formula function
#which will print the distance using the format of [x1,y1,x2,y2]
def distance(lst):
    print(int((((int(lst[0])-int(lst[2]))**2  +(int(lst[1])-int(lst[3]))**2)**.5)))
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break   
    distance("".join([i for i in test if i.isdigit() or i=="-" or i==" "]).split(" "))
test_cases.close()
