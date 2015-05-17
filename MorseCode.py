##status: Solved
##Problem: https://www.codeeval.com/open_challenges/116/
##You have received a text encoded with Morse code and want to decode it.

#This second is just to create a dictionary to translate morse code to the alphabet. the first line is the output of they key on an online morse code translator
#Since a double space will space out as an empty string, i added "":" " to the dictionary since a double space is a space between words
MorseCode = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----."
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MorseCode = dict([[MorseCode.split(" ")[i], key[i]] for i in range(0,len(key))])
MorseCode.update({"":" "})


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    print("".join([MorseCode[i] for i in test[:-1].split(" ")]))
test_cases.close()
