# Code-Eval-Challenges
challenge problems found on codeeval
for i in range(1,13):
    for j in range(1,13):
        for k in range(4-len(str(i*(j)))):
            print(end = " ")
        print (i*j, end = "")
        
    print()
