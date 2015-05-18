##status: Solved
##Problem: https://www.codeeval.com/open_challenges/124/
##You've decided to make a road trip across the country in a straight line. You have chosen the direction you'd like to travel and made a list of cities in that direction that have gas stations to stop at and fill up your tank. To make sure that this route is viable, you need to know the distances between the adjacent cities in order to be able to travel this distance on a single tank of gasoline, (No one likes running out of gas.) but you only know distances to each city from your starting point.


#So this will just take the distances or the numbers into account and add your location(0 distance away)
#it will then sort them in order and print the distances from one point to the next via the difference
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    test = [int(i[i.index(",")+1:]) for i in test[:-2].split(";")]+[0]
    test.sort()
    print(",".join([str(test[i]-test[i-1]) for i in range(1,len(test))]))
test_cases.close()
