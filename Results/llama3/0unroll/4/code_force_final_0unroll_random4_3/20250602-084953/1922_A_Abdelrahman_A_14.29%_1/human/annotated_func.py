#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each of length n, consisting of lowercase Latin letters.
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
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case. If string c contains any character not present in strings a or b, 'YES' will be printed for that test case. Otherwise, 'NO' will be printed. The value of the variable 'tests' remains unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings a, b, and c. It then checks if string c contains any character not present in strings a or b. If such a character is found, it prints 'YES' to the console; otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results, leaving the input variable 'tests' unchanged.

