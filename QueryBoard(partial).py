matrix = [[j for i in range(0,256)] for j in range(0,256)]

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test =="":
        break
    line = int(test[:-1].split(" ")[1])
    if "Set" in test:
        value = int(test[:-1].split(" ")[2])

    if "SetRow" in test:
        matrix[line] = [value for i in range(0,256)]
    elif "SetCol" in test:
        for i in range(0,256):
            matrix[i][line]=value
    elif "QueryRow" in test:
        print(sum(matrix[line]))
    else:
        print(sum([matrix[i][line] for i in range(0,256)]))

test_cases.close()
