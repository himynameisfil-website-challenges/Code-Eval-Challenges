##Status: solved
##problem: https://www.codeeval.com/open_challenges/103/
##There is a game where each player picks a number from 1 to 9, writes it on a paper and gives to a guide. A player wins if his number is the lowest unique. We may have 10-20 players in our game.
##
##solution: The core of the program is in the winner function, which will make an array of all the numbers,
##find the value of the smallest number that only appears once, then determines which player has it.
##if there are no unique numbers, it just prints 0
def winner(message):
    message = message[:-1].split(" ")
    try:
        print(message.index(min([i for i in message if message.count(i)==1]))+1)
    except:
        print(0)
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    winner(test)
test_cases.close()
