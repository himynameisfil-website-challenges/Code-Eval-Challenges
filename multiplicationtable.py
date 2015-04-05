##Status:Solved
##Problem:https://www.codeeval.com/open_challenges/23/
##Print out the grade school multiplication table upto 12*12.

for i in range(1,13):
    for j in range(1,13):
        for k in range(4-len(str(i*(j)))):
            print(end = " ")
        print (i*j, end = "")
        
    print()
