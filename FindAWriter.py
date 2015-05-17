#status: solved
#Problem: https://www.codeeval.com/open_challenges/97/
#You have a set of rows with names of famous writers encoded inside. Each row is divided into 2 parts by pipe char (|). The first part has a writer's name. The second part is a "key" to generate a name.
#Your goal is to go through each number in the key (numbers are separated by space) left-to-right. Each number represents a position in the 1st part of a row. This way you collect a writer's name which you have to output.


#Solution: So I split the mesage into two parts, the cipher and the key. they cipher is just an array of the first half(w/ the | as the divider) and the index/key as each number in the second half. Then decrypts the message via indexing
def SecretCode(message):
    cipher = message.split("|")[0]
    key = [int(i) for i in message[:-1].split("|")[1][1:].split(" ")]
    return "".join([cipher[i-1] for i in key])

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print(SecretCode(test))
test_cases.close()
