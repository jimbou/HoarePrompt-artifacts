#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: The loop will print 'YES' or 'NO' for each test case, indicating whether the string c can be formed by taking characters from strings a and b, with the constraint that each character in c must be taken from the same position in either a or b. The output will be a series of 'YES' or 'NO' statements, one for each test case. The value of the variable 'tests' will remain unchanged, and the contents of stdin will be consumed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and three strings a, b, and c, each of length n. It then checks whether the string c can be formed by taking characters from strings a and b, with the constraint that each character in c must be taken from the same position in either a or b. For each test case, it prints 'YES' if c can be formed and 'NO' otherwise. The function consumes the contents of standard input and does not modify any external state.

