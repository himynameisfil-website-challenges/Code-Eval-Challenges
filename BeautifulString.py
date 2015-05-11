##Status: Solved
##https://www.codeeval.com/open_challenges/83/
##You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?



import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
#This will truncate the new line code "\n" and lowercase everything
    test = test[:-1].lower()
#this will create a list that will count how many times a letter shows up in the input
#It will only add it to the list if it's a letter and it wasn't counted before    
    lst = [test.count(test[i]) for i in range(0,len(test)) if test[i].isalpha() and test.index(test[i])==i]
#Sort and reverse, then it will take the largest count, multiply it by 26, 2nd largest*25, etc. and take the sum of those numbers
    lst.sort(reverse = True)
    print(sum([(26-i)*lst[i] for i in range(0,len(lst))]))

test_cases.close()
